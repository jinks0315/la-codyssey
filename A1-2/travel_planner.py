import os
import json
import argparse
from datetime import datetime

import requests
from dotenv import load_dotenv
from google import genai


# =========================
# 1. 환경변수
# =========================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")

if not GEMINI_API_KEY:
    print("오류: GEMINI_API_KEY가 설정되지 않았습니다.")
    exit()

if not KAKAO_API_KEY:
    print("오류: KAKAO_API_KEY가 설정되지 않았습니다.")
    exit()


client = genai.Client(api_key=GEMINI_API_KEY)


# =========================
# 2. 날짜 검증
# =========================

def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# =========================
# 3. Gemini 여행지 추천
# =========================

def get_travel_recommendation(date):
    prompt = f"""
사용자의 여행 날짜는 {date}입니다.

이 날짜에 대한민국에서 여행하기 좋은 지역 1곳을 추천해주세요.

반드시 아래 JSON 형식으로만 답변하세요.

{{
    "recommended_city": "지역명",
    "weather": "해당 시기의 일반적인 날씨 설명",
    "events": ["행사 또는 축제 1", "행사 또는 축제 2"],
    "reason": "추천 이유를 2~4문장으로 설명"
}}

조건:
- JSON 이외의 설명을 출력하지 마세요.
- Markdown 코드 블록을 사용하지 마세요.
- recommended_city는 대한민국 지역명 1개만 작성하세요.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    return json.loads(text)


# =========================
# 4. Kakao 맛집 검색
# =========================

def search_restaurants(city):
    url = "https://dapi.kakao.com/v2/local/search/keyword.json"

    headers = {
        "Authorization": f"KakaoAK {KAKAO_API_KEY}"
    }

    params = {
        "query": f"{city} 맛집",
        "size": 5
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    restaurants = []

    for item in data.get("documents", []):
        restaurants.append({
            "name": item.get("place_name"),
            "address": (
                item.get("road_address_name")
                or item.get("address_name")
            ),
            "category": item.get("category_name"),
            "url": item.get("place_url"),
            "x": item.get("x"),
            "y": item.get("y")
        })

    return restaurants


# =========================
# 5. Gemini 최종 리포트
# =========================

def create_final_report(
    date,
    recommendation,
    restaurants,
    errors
):

    recommendation_json = json.dumps(
        recommendation,
        ensure_ascii=False,
        indent=2
    )

    restaurants_json = json.dumps(
        restaurants,
        ensure_ascii=False,
        indent=2
    )

    errors_json = json.dumps(
        errors,
        ensure_ascii=False,
        indent=2
    )

    prompt = f"""
다음 정보를 이용하여 국내 여행 추천 리포트를 작성해주세요.

여행 날짜:
{date}

여행 추천 정보:
{recommendation_json}

맛집 검색 결과:
{restaurants_json}

오류 정보:
{errors_json}

반드시 Markdown 형식으로 작성해주세요.

아래 구조를 사용하세요.

# {date} 국내 여행 추천 리포트

## 추천 지역

## 추천 이유

## 날씨 요약

## 행사/축제

## 맛집 추천

## 1일 일정 제안

## 오류 요약(errors)

조건:
- 맛집 검색 결과가 없으면 "데이터 없음"이라고 작성하세요.
- 오류가 없으면 "없음"이라고 작성하세요.
- 일정은 오전 / 오후 / 저녁으로 나누세요.
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return response.text.strip()


# =========================
# 6. 결과 저장
# =========================

def save_results(
    date,
    recommendation,
    restaurants,
    errors,
    report
):

    os.makedirs("results", exist_ok=True)

    raw_data = {
        "date": date,
        "recommendation": recommendation,
        "restaurants": restaurants,
        "errors": errors
    }

    json_path = f"results/{date}_data.json"

    with open(
        json_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            raw_data,
            file,
            ensure_ascii=False,
            indent=2
        )

    report_path = f"results/{date}_travel_plan.md"

    with open(
        report_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    return json_path, report_path


# =========================
# 7. 메인
# =========================

def main():

    parser = argparse.ArgumentParser(
        description="국내 여행지 추천 프로그램"
    )

    parser.add_argument(
    "-date",
    "--date",
    dest="date",
    required=True,
    help='여행 날짜 YYYY-MM-DD'
    )
    args = parser.parse_args()


    # 날짜 검사

    if not validate_date(args.date):

        print("오류: 날짜 형식이 올바르지 않습니다.")

        print(
            '사용법: .venv/bin/python '
            'travel_planner.py '
            '--date "YYYY-MM-DD"'
        )

        return


    errors = []


    # =========================
    # 1/3 여행지 추천
    # =========================

    print("[1/3] 1차 추천 생성 중(Gemini)...")

    recommendation = None

    try:

        recommendation = get_travel_recommendation(
            args.date
        )

    except json.JSONDecodeError:

        print("JSON 파싱 실패. 한 번 더 요청합니다.")

        errors.append({
            "step": "recommendation",
            "type": "JSON_PARSE_ERROR",
            "message": "첫 번째 Gemini JSON 파싱 실패"
        })

        try:

            recommendation = get_travel_recommendation(
                args.date
            )

        except Exception as error:

            print("재시도에 실패했습니다.")
            print(error)

            return

    except Exception as error:

        print("Gemini API 호출에 실패했습니다.")
        print(error)

        return


    city = recommendation.get(
        "recommended_city"
    )

    print(f"- 추천 지역: {city}")


    # =========================
    # 2/3 맛집 검색
    # =========================

    print()
    print("[2/3] 맛집 검색 중(Kakao Local)...")

    restaurants = []

    try:

        restaurants = search_restaurants(city)

        if not restaurants:

            print("- 검색 결과 0건")
            print("- 데이터 없음으로 계속 진행합니다.")

            errors.append({
                "step": "place_search",
                "type": "EMPTY_RESULT",
                "message": (
                    f"0 results for "
                    f"query={city} 맛집"
                )
            })

        else:

            print(
                f"- 맛집 {len(restaurants)}곳 검색 완료"
            )

    except requests.exceptions.HTTPError as error:

        print("- Kakao API HTTP 오류")
        print("- 맛집은 데이터 없음으로 처리합니다.")

        errors.append({
            "step": "place_search",
            "type": "HTTP_ERROR",
            "message": str(error)
        })

        restaurants = []

    except requests.exceptions.RequestException as error:

        print("- Kakao API 네트워크 오류")
        print("- 맛집은 데이터 없음으로 처리합니다.")

        errors.append({
            "step": "place_search",
            "type": "NETWORK_ERROR",
            "message": str(error)
        })

        restaurants = []

    except Exception as error:

        print("- 맛집 검색 오류")
        print("- 데이터 없음으로 처리합니다.")

        errors.append({
            "step": "place_search",
            "type": "UNKNOWN_ERROR",
            "message": str(error)
        })

        restaurants = []


    # =========================
    # 3/3 최종 리포트
    # =========================

    print()
    print("[3/3] 최종 리포트 생성 중(Gemini)...")

    try:

        report = create_final_report(
            args.date,
            recommendation,
            restaurants,
            errors
        )

    except Exception as error:

        print("최종 리포트 생성 실패")
        print(error)

        return


    # =========================
    # 파일 저장
    # =========================

    json_path, report_path = save_results(
        args.date,
        recommendation,
        restaurants,
        errors,
        report
    )


    print("- 리포트 생성 완료")

    print()
    print("완료!")
    print(f"원본 JSON: {json_path}")
    print(f"최종 리포트: {report_path}")


# =========================
# 실행
# =========================

if __name__ == "__main__":
    main()