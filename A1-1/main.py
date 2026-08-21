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


def show_prompt_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite_mark}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    categories = []

    for prompt in prompts:
        category = prompt["category"]

        if category not in categories:
            categories.append(category)

    if not categories:
        print("등록된 카테고리가 없습니다.")
        return

    for index, category in enumerate(categories, start=1):
        print(f"{index}. {category}")

    choice = input("\n카테고리 번호를 선택하세요: ").strip()

    if not choice.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    category_index = int(choice) - 1

    if category_index < 0 or category_index >= len(categories):
        print("존재하지 않는 카테고리입니다.")
        return

    selected_category = categories[category_index]

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            filtered_prompts.append(prompt)

    print(f"\n=== [{selected_category}] 프롬프트 ===")

    if not filtered_prompts:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"{prompt['title']}"
            f"{favorite_mark}"
        )

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")


def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = get_non_empty_input("검색어: ").lower()

    results = []

    for prompt in prompts:
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for index, prompt in enumerate(results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite_mark}"
        )

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")


def show_prompt_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. "
            f"[{prompt['category']}] "
            f"{prompt['title']}"
            f"{favorite_mark}"
        )

    choice = input("\n상세 보기할 프롬프트 번호: ").strip()

    if not choice.isdigit():
        print("올바른 번호를 입력해주세요.")
        return

    prompt_index = int(choice) - 1

    if prompt_index < 0 or prompt_index >= len(prompts):
        print("존재하지 않는 프롬프트 번호입니다.")
        return

    selected_prompt = prompts[prompt_index]

    favorite_text = "등록됨 ⭐" if selected_prompt["favorite"] else "등록되지 않음"

    print("\n=== 프롬프트 상세 정보 ===")
    print(f"제목: {selected_prompt['title']}")
    print(f"카테고리: {selected_prompt['category']}")
    print(f"내용: {selected_prompt['content']}")
    print(f"즐겨찾기: {favorite_text}")


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

        elif choice == "2":
            show_prompt_list()

        elif choice == "3":
            show_by_category()

        elif choice == "4":
            search_prompt()

        elif choice == "5":
            show_prompt_detail()

        elif choice == "8":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["6", "7"]:
            print("아직 구현되지 않은 기능입니다.")

        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()