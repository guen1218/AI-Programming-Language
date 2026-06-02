from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['종료', '내 계좌 목록', '입금', '출금', '계좌 개설', '계좌 삭제', '내 정보 관리']
    member_myinfo_menu = ['종료', '내 정보 보기', '비밀번호 변경', '회원 탈퇴']
    admin_menu = ['종료', '회원 관리 메뉴', '계좌 관리 메뉴']
    admin_account_menu = ['종료', '전체 계좌 목록', '특정 회원 계좌']
    admin_member_menu = ['종료', '전체 회원 목록', '특정 회원 조회', '회원 강제 탈퇴']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())

    def main(self):
        self.show_welcome()
        while True:
            # 기존 select_menu 전달 오류 수정 (클래스 메서드 참조 대신 인스턴스 메뉴 목록 전달)
            menu = self.select_menu(ConsoleBank.start_menu)
            if menu == 0: 
                break
            elif menu == 1:
                # 로그인 구현 공간 (성공 시 권한에 따라 뱅킹 혹은 관리자 메뉴 호출하도록 유도)
                print("로그인")
                user_type = input("1. 일반회원 / 2. 관리자 : ")
                if user_type == "1":
                    self.run_banking_menu()
                elif user_type == "2":
                    self.run_admin_menu() # self인자 중복 제거
            elif menu == 2:
                print("회원가입")
            else: 
                print("다시하시오")
        self.say_goodbye()


#======================================= user

    def run_banking_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.banking_menu)
            if menu == 0: 
                break
            elif menu == 1:
                pass  # 내 계좌 목록
            elif menu == 2:
                pass  # 입금
            elif menu == 3:
                pass  # 출금
            elif menu == 4:
                pass  # 계좌 개설
            elif menu == 5:
                pass  # 계좌 삭제
            elif menu == 6:
                self.run_my_info_menu()  # 내 정보 관리 메뉴 호출
            else: 
                print("다시하시오")

    def run_my_info_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.member_myinfo_menu)
            if menu == 0: 
                break
            elif menu == 1:
                pass  # 내 정보 보기
            elif menu == 2:
                pass  # 비밀번호 변경
            elif menu == 3:
                pass  # 회원 탈퇴
            else: 
                print("다시하시오")

#======================================= user

#======================================= admin

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_menu)
            if menu == 0: 
                break
            elif menu == 1:
                self.run_admin_member_menu()  # 회원 관리 메뉴 호출
            elif menu == 2:
                self.run_admin_account_menu()  # 계좌 관리 메뉴 호출
            else: 
                print("다시하시오")

    def run_admin_account_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_account_menu)
            if menu == 0: 
                break
            elif menu == 1:
                pass  # 전체 계좌 목록
            elif menu == 2:
                pass  # 특정 회원 계좌
            else: 
                print("다시하시오")

    def run_admin_member_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.admin_member_menu)
            if menu == 0: 
                break
            elif menu == 1:
                pass  # 전체 회원 목록
            elif menu == 2:
                pass  # 특정 회원 조회
            elif menu == 3:
                pass  # 회원 강제 탈퇴
            else: 
                print("다시하시오")

#======================================= admin

    def show_welcome(self):
        print('======== Hyejeong Console Bank ==========')

    def say_goodbye(self):
        print('>> Hyejeong Console Bank를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        # 0번 종료 출력을 직관적으로 표현하고 줄바꿈(\t) 오타 수정
        for i in range(len(menu_list)):
            print(f"{i}. {menu_list[i]}", end="   ")
        print() # 입력창 전 줄바꿈
        return int(input("메뉴를 선택하시오 : "))

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()