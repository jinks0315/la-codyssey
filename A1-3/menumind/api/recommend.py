from http.server import BaseHTTPRequestHandler
from openai import OpenAI
import json
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
    base_url="https://copa.codyssey.kr/v1"
)


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            ingredients = data.get("ingredients", "").strip()
            difficulty = data.get("difficulty", "쉬움")
            cooking_time = data.get("time", "30분 이하")

            if not ingredients:
                self.send_response(400)
                self.send_header(
                    "Content-Type",
                    "application/json; charset=utf-8"
                )
                self.end_headers()

                self.wfile.write(
                    json.dumps({
                        "success": False,
                        "message": "재료를 입력해주세요."
                    }, ensure_ascii=False).encode("utf-8")
                )
                return

            prompt = f"""
사용자가 가지고 있는 재료를 이용해서
만들 수 있는 요리 하나를 추천해주세요.

가지고 있는 재료:
{ingredients}

원하는 난이도:
{difficulty}

원하는 조리 시간:
{cooking_time}

다음 형식으로 한국어로 답변해주세요.

🍳 추천 요리:
⏱ 예상 조리 시간:
🥕 필요한 재료:
👨‍🍳 조리 방법:
1.
2.
3.
4.

가능하면 사용자가 입력한 재료를 우선 사용해주세요.
설명은 요리 초보자도 이해하기 쉽게 작성해주세요.
"""

            response = client.chat.completions.create(
                model="gpt-5-mini",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            ai_result = response.choices[0].message.content

            response_data = {
                "success": True,
                "result": ai_result
            }

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps(
                    response_data,
                    ensure_ascii=False
                ).encode("utf-8")
            )

        except Exception as e:
            print("ERROR:", str(e))

            self.send_response(500)
            self.send_header(
                "Content-Type",
                "application/json; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(
                json.dumps({
                    "success": False,
                    "message": "AI 추천 중 오류가 발생했습니다."
                }, ensure_ascii=False).encode("utf-8")
            )