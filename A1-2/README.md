# 국내 여행지 추천 프로그램

## 1. 프로그램 개요

사용자가 여행 날짜를 입력하면 Gemini API를 활용하여 해당 시기에 여행하기 좋은 국내 지역을 추천하고, Kakao Local API를 이용하여 추천 지역의 맛집을 검색하는 프로그램입니다.

여행지 추천 정보와 맛집 검색 결과를 조합하여 최종 여행 리포트를 Markdown 형식으로 생성합니다.

### 프로그램 동작 흐름

1. 사용자가 여행 날짜 입력
2. Gemini API를 이용하여 여행 지역 추천
3. 추천 결과를 JSON 형식으로 변환
4. 추천된 지역을 이용하여 Kakao Local API에서 맛집 검색
5. 여행 추천 정보와 맛집 정보를 Gemini API에 전달
6. 최종 여행 리포트 생성
7. JSON 및 Markdown 파일을 `results/` 폴더에 저장

---

## 2. 개발 환경

* Python 3.12
* Google Gemini API
* Kakao Local API

사용 Python 라이브러리:

* google-genai
* requests
* python-dotenv

---

## 3. 설치 방법

프로젝트 폴더에서 가상환경을 생성합니다.

```bash
python3 -m venv .venv
```

macOS/Linux에서 가상환경을 활성화합니다.

```bash
source .venv/bin/activate
```

필요한 라이브러리를 설치합니다.

```bash
python -m pip install google-genai requests python-dotenv
```

---

## 4. API 키 설정

프로젝트 최상위 폴더에 `.env` 파일을 생성합니다.

```text
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
KAKAO_API_KEY=YOUR_KAKAO_REST_API_KEY
```

실제 API 키 값은 코드나 README 파일에 직접 작성하지 않습니다.

---

## 5. 실행 방법

다음과 같이 여행 날짜를 `YYYY-MM-DD` 형식으로 입력하여 프로그램을 실행합니다.

```bash
python travel_planner.py -date "2026-09-15"
python travel_planner.py --date "2026-09-15"
```

가상환경의 Python을 직접 사용하는 경우:

```bash
.venv/bin/python travel_planner.py -date "2026-09-15"
.venv/bin/python travel_planner.py --date "2026-09-15"
```

정상적으로 실행되면 다음과 같은 과정이 진행됩니다.

```text
[1/3] 1차 추천 생성 중(Gemini)...
- 추천 지역: 평창

[2/3] 맛집 검색 중(Kakao Local)...
- 맛집 5곳 검색 완료

[3/3] 최종 리포트 생성 중(Gemini)...
- 리포트 생성 완료
```

---

## 6. 결과물 확인

프로그램 실행이 완료되면 `results/` 폴더에 결과 파일이 생성됩니다.

예:

```text
results/
├── 2026-09-15_data.json
└── 2026-09-15_travel_plan.md
```

### JSON 파일

원본 실행 데이터를 저장합니다.

포함되는 주요 데이터:

* 여행 날짜
* 추천 지역
* 날씨 정보
* 행사/축제 정보
* 추천 이유
* 맛집 검색 결과
* 오류 정보

### Markdown 파일

최종 여행 추천 리포트를 저장합니다.

리포트에는 다음 내용이 포함됩니다.

* 추천 지역
* 추천 이유
* 날씨 요약
* 행사/축제
* 맛집 추천
* 1일 일정 제안
* 오류 요약

---

## 7. 오류 처리

프로그램은 다음과 같은 오류 상황을 처리합니다.

* 잘못된 날짜 형식
* API 키 미설정
* Gemini API 호출 실패
* Gemini JSON 파싱 실패
* Kakao Local API 호출 실패
* 네트워크 오류
* 맛집 검색 결과가 없는 경우

맛집 검색에 실패하더라도 맛집 데이터를 빈 목록으로 처리하고 최종 리포트 생성을 계속 진행합니다.

Gemini의 JSON 응답을 파싱하지 못한 경우 최대 1회 다시 요청합니다.

---

## 8. API 키 보안 주의사항

API 키는 소스 코드에 직접 작성하지 않고 `.env` 파일을 통해 관리합니다.

`.gitignore`에는 다음 항목을 추가합니다.

```text
.env
.venv/
__pycache__/
```

이를 통해 Git 저장소에 API 키가 포함되는 것을 방지합니다.

API 키는 외부에 공개하거나 GitHub 등의 공개 저장소에 업로드하지 않도록 주의해야 합니다.
