from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Account.account import Account
from Account.account_dao import AccountDAO
from Account.account_service import AccountService

class ConsoleBank:
    start_menu = ['종료', '로그인', '회원가입']
    banking_menu = ['로그아웃', '내 계좌 목록', '입금', '출금', '계좌 개설', '계좌 해지', '내 정보 관리']
    member_myinfo_menu = ['뒤로가기', '비밀번호 변경', '회원 탈퇴']
    admin_menu = ['로그아웃', '회원 관리 메뉴', '계좌 관리 메뉴']
    admin_account_menu = ['뒤로가기', '전체 계좌 목록', '회원별 계좌 목록']
    admin_member_menu = ['뒤로가기', '회원 목록', '회원 정보 조회', '회원 강퇴']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.asv = AccountService(AccountDAO())
        self.msv.join(Member('a', 'a', 'a'))
        self.msv.join(Member('b', 'b', 'b'))
        self.asv.create_account(Account(0, 'a', 10000, 'a'))
        self.asv.create_account(Account(0, 'b', 100200, 'b'))

    def main(self):
        self.show_welcome()
        menu = self.select_menu(ConsoleBank.start_menu)
        self.run_start_menu(menu)
        self.say_goodbye()

    def run_start_menu(self, menu):
        while True:
            if menu == 0:  # 끝
                break
            elif menu == 1:
                self.menu_login() # 로그인
            elif menu == 2:
                self.menu_join() # 회원가입
            else: 
                print("다시하시오")
            menu = self.select_menu(ConsoleBank.start_menu)

    def show_welcome(self):
        print('======== GH Console Bank ==========')
    def say_goodbye(self):
        print('>> GH Console Bank를 이용해 주셔서 감사합니다.')

    def select_menu(self, menu_list):
        print('-'*50)
        for index in range(1, len(menu_list)):
            print(f"{index}. {menu_list[index]}", end="   ")
        print(f"0. {menu_list[0]}")
        print('-'*50)
        try:
            num = int(input(">> 메뉴 : "))
        except ValueError:
            return -1
        else:
            return num

    def menu_login(self):
        print(">>>>>>>> 로그인 <<<<<<<<<")
        id = input("아이디 : ")
        pw = input("비밀번호 : ")
        if self.msv.login(id, pw):
            print(f'{self.msv.view_member_info(id).get_name()}님, 환영합니다.')
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_banking_menu()
        else:
            print("로그인 실패")
        
    def menu_join(self):
        print('>>>>> 회원가입 <<<<<')
        name = input("이름: ")
        id = input("아이디: ")
        pw = input("비밀번호: ")
        if self.msv.join(Member(id, pw, name)):
            print('회원가입 성공')
        else : 
            print('회원가입 실패')
        
#======================================= user 

    def run_banking_menu(self):
        while True:
            menu = self.select_menu(ConsoleBank.banking_menu)
            if menu == 0: 
                break
            elif menu == 1:
                self.list_members_accounts()  # 내 계좌 목록
            elif menu == 2:
                self.menu_deposit()  # 입금
            elif menu == 3:
                self.menu_withdraw()  # 출금
            elif menu == 4:
                self.menu_create_account()  # 계좌 개설
            elif menu == 5:
                self.menu_delete_account()  # 계좌 삭제
            elif menu == 6:
                if self.run_my_info_menu() == "backhome" :  # 내 정보 관리 메뉴 호출
                    break
            else: 
                print("다시하시오")
        self.msv.current_user = None

#======================run_banking_menu========================================= ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

    def list_members_accounts(self): # 1
        account_list = self.asv.get_members_accounts(self.msv.current_user)
        if account_list:
            print('------------------------------------')
            for account in account_list:
                print(account)
            print('------------------------------------')    
        else:
            print('등록된 계좌가 없습니다')
        return account_list

    def menu_deposit(self): # 2 입금
        print('>>>>입금<<<<')
        if not self.list_members_accounts():
            return
        account_no = input('>> 계좌번호 : ')
        amount = int(input("입금액 : "))
        if self.asv.deposit(account_no, amount):
            print(f'계좌번호 {account_no}에 {amount}원을 입금했습니다.')
            balance = self.asv.get_account_balance(account_no)
            if balance >= 0:
                print(f'잔액 : {balance}')
        else: 
            print("실패")

    def menu_withdraw(self): # 3 출금
        print('>>>>출금<<<<')
        if not self.list_members_accounts():
            return
        id = input("아이디 : ")
        account_no = input('>> 계좌번호 : ')
        amount = int(input("출금액 : "))
        password = input("비밀번호 : ")
        try:
            self.asv.withdraw(id, account_no, amount, password)
        except LookupError:
            print("계좌를 찾을 수 없습니다")
        except KeyError:
            print("실패")
        except ValueError:
            print("잔액이 부족합니다")
        else:
            print(f'계좌번호 {account_no}에 {amount}원을 출금했습니다.')
            balance = self.asv.get_account_balance(account_no)
            print(f'잔액 : {balance}')

    def menu_create_account(self): # 4 계좌생성
        print('>>>>계좌생성<<<<')
        balance = int(input("초기 금액: "))
        if balance < 1000 :
            print("1000 이상을 입력해주세요")
            return
        password = input("계좌 비밀번호 : ")
        account = Account(0, self.msv.current_user, balance, password)
        if self.asv.create_account(account):
            print("성공")
        else:
            print("실패")
    
    def menu_delete_account(self): # 5 계좌해지
        print('>>>>계좌해지<<<<')
        account_no = int(input("계좌번호 입력: "))
        password = input("계좌 비밀번호 입력 : ")
        try: 
            self.asv.delete_account(self.msv.current_user, account_no, password)
        except LookupError:
            print("계좌 찾기 실패")
        except KeyError:
            print("비번이 틀렸습니다")
        except TypeError:
            print("돈 다 빼세요")
        else:
            print("성공") 

    def menu_myinfo(self): # 6 내정보
        print('>>>>내정보<<<<')
        if self.run_my_info_menu() == "backhome":
            return "backhome"
        
#===================run_banking_menu============================================ ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑

    def run_my_info_menu(self):
        self.menu_view_myinfo() # 내 정보 보기
        while True:
            menu = self.select_menu(ConsoleBank.member_myinfo_menu)
            if menu == 0: 
                break
            elif menu == 1:
                self.menu_update_password()  # 비밀번호 변경
            elif menu == 2:
                if self.menu_delete_membership() == "backhome" : # 회원 탈퇴
                    return "backhome"
            else: 
                print("다시하시오")

# ========================================================================

    def menu_view_myinfo(self): # 내 정보 보기
        print('------------------------------------')
        print(self.msv.view_member_info(self.msv.current_user))
        print('------------------------------------')

    def menu_update_password(self): # 비밀번호 변경
        print('>>>>비밀번호 변경<<<<')
        id = input('>> 아이디 입력 : ')
        org_password = input('>> 기존 비밀번호 입력 : ')
        new_password = input('>> 새 비밀번호 입력 : ')
        if self.msv.update_member_password(id, org_password, new_password):
            print("변경 성공~")
            return "backhome"
        print("변경 실패")

    def menu_delete_membership(self): # 회원 탈퇴
        print('>>>>회원 탈퇴<<<<')
        id = input('>> 아이디 입력 : ')
        if self.msv.remove_member(id):
            print("탈퇴 성공~")
            return "backhome"
        print("탈퇴 실패")

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
        self.msv.current_user = None

# ========================================

    def run_admin_member_menu(self):
        print('>>>>회원 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(ConsoleBank.admin_member_menu)
            if menu == 0: 
                break
            elif menu == 1:
                self.menu_list_members()  # 회원 목록
            elif menu == 2:
                self.menu_view_member_info()  # 회원 정보 조회
            elif menu == 3:
                self.menu_delete_member()  # 회원 강퇴
            else: 
                print("다시하시오")

# ========================================

    def menu_list_members(self):
        if self.msv.current_user != MemberService.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        print('>>>>회원 목록<<<<')
        mem_list = self.msv.list_members()[1:]
        if mem_list:
            print('------------------------------------')
            for member in mem_list:
                print(member)
            print('------------------------------------')
        else:
            print('등록된 회원이 없습니다')

    def menu_view_member_info(self):
        if self.msv.current_user != MemberService.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        print('>>>>회원 정보 조회<<<<')
        self.menu_list_members()
        id = input(">> 조회할 회원 id 입력")
        print(self.msv.view_member_info(id))

    def menu_delete_member(self):
        if self.msv.current_user != MemberService.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        print('>>>>회원 강퇴<<<<')
        self.menu_list_members()
        id = input(">> 강퇴할 회원 id 입력")
        if self.msv.remove_member(id): 
            print("강퇴 성공~")
            return
        print("강퇴 실패")

# ========================================
# ========================================

    def run_admin_account_menu(self):
        print('>>>>계좌 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(ConsoleBank.admin_account_menu)
            if menu == 0: 
                break
            elif menu == 1:
                self.menu_list_all_accounts()  # 전체 계좌 목록
            elif menu == 2:
                self.menu_list_member_accounts()  # 회원별 계좌 목록
            else: 
                print("다시하시오")

# ========================================

    def menu_list_all_accounts(self):
        if self.msv.current_user != MemberService.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        print('>>>>전체 계좌 목록<<<<')
        account_list = self.asv.get_all_accounts()
        if account_list:
            print('------------------------------------')
            for account in account_list:
                print(account)
            print('------------------------------------')
        else:
            print("계좌가 존재하지 않습니다.")

    def menu_list_member_accounts(self):
        if self.msv.current_user != MemberService.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        print('>>>>회원별 계좌 목록<<<<')
        mem_account_list = self.msv.list_members()[1:]
        if mem_account_list:
            print('------------------------------------')
            for account in mem_account_list:
                name = account.get_name()
                id = account.get_id()
                print(f"{name}님의 계좌 : {self.asv.get_members_accounts(id)}")
            print('------------------------------------')
        else:
            print("계좌가 존재하지 않습니다.")

#======================================= admin

if __name__ == '__main__':
    app = ConsoleBank()
    app.main()