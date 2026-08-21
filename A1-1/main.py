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


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("빈 값은 입력할 수 없습니다. 다시 입력해주세요.")


def add_prompt():
    print("\n=== 프롬프트 추가 ===")

    title = get_non_empty_input("제목: ")
    content = get_non_empty_input("내용: ")
    category = get_non_empty_input("카테고리: ")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    }

    prompts.append(new_prompt)

    print("\n프롬프트가 추가되었습니다!")


def show_menu():
    print("\n=== 프롬프트 관리 프로그램 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("8. 종료")


def main():
    while True:
        show_menu()

        choice = input("\n메뉴를 선택하세요: ").strip()

        if choice == "1":
            add_prompt()

        elif choice == "8":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["2", "3", "4", "5", "6", "7"]:
            print("아직 구현되지 않은 기능입니다.")

        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()