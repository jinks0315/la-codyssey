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

        if choice == "8":
            print("프로그램을 종료합니다.")
            break

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("아직 구현되지 않은 기능입니다.")

        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()