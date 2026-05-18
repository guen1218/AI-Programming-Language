from member import MemberService
ms = MemberService()

while True:
    print("="*10)
    print("회원 관리")
    print("="*30)
    print("1. 회원가입")
    print("2. 회원목록")
    print("3. 상세정보조회")
    print("4. 회원정보수정")
    print("5. 회원탈퇴")
    print("0. 프로그램 종료")
    print("="*10)

    choice = input("원하는 메뉴 번호를 입력하세요: ").strip()
    if choice == '1':
        print("\n--- 회원 가입 ---")
        num = input("번호: ")
        id_ = input("아이디: ")
        pas = input("비밀번호: ")
        name = input("이름: ").strip()
        pon = input("전화번호: ")
        add = input("주소: ")
        if ms.create_mem(num, id_, pas, name, pon, add) :
            print(f"[{name}] 가입 성공")
        else:
            print("가입 실패")

    elif choice == '2':
        ms.see_mem()

    elif choice == '3':
        name = input("조회할 이름을 입력하세요: ")
        result = ms.super_see_mem(name)
        if result:
            print(result)
        else:
            print("누구세요")

    elif choice == '4':
        name = input("수정할 회원의 이름을 입력하세요: ")
        item = input("수정할 항목(id, name, pon, add): ")
        new_data = input("새로운 내용: ")
        if ms.update_mem(name, item, new_data):
            print("수정 성공")
        else:
            print("수정 실패")

    elif choice == '5':
        name = input("탈퇴할 회원의 이름을 입력하세요: ")
        if ms.delete_mem(name):
            print(f"{name}님 탈퇴")
        else:
            print("탈퇴 실패")

    elif choice == '0':
        print("프로그램 종료")
        break

    else:
        print("다시하세요")