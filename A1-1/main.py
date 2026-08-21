prompts = [
    {
        "title": "파이썬 코드 리뷰",
        "category": "개발",
        "content": "다음 파이썬 코드를 리뷰하고 개선할 점을 알려줘.",
        "favorite": False,
    },
    {
        "title": "여행 일정 만들기",
        "category": "여행",
        "content": "여행지와 기간을 바탕으로 효율적인 여행 일정을 만들어줘.",
        "favorite": False,
    },
    {
        "title": "글 요약하기",
        "category": "학습",
        "content": "다음 글의 핵심 내용을 이해하기 쉽게 요약해줘.",
        "favorite": True,
    },
]


def main():
    print("프롬프트 관리 프로그램")
    print(f"현재 저장된 프롬프트: {len(prompts)}개")


if __name__ == "__main__":
    main()