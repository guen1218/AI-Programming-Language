from account import AccountService

#메뉴와 사용자 interaction에 따른 서비스 호출
def select_menu():
    print('='*50)
    print(' 1. 계좌생성 | 2. 계좌목록 | 3. 입금 | 4. 출금 | 0. 종료')
    print('='*50)
    return int(input(">메뉴 선택"))

def start_console_bank():
    print()
    print('='*10, " BANK ", '='*10)
    while True:
        menu = select_menu()
        if menu == 0 : break
        elif menu == 1:
            # 계좌번호, 계좌주, 잔액 입력을 받아서 계좌 생성
            account_no = input("> 계좌번호 : ")
            owner = input("> 계좌주 : ") 
            balance = int(input("> 초기 입금액 : "))
            if aservice.create_account(account_no, owner, balance):
                print("결과 : 계좌가 생성되었습니다.")
        elif menu == 2 : # 계좌 목록
            account_list = aservice.list_account()
            print("--------------")
            print("-- 계좌 목록 --")
            print("--------------")
            for account in account_list:
                print (account)

        elif menu == 3 : #입금
            print("--------------")
            print("---- 예금 ----")
            print("--------------")
            account_no = input("> 계좌번호")
            amount = int(input("> 예금액 : "))
            aservice.deposit(account_no, amount)

        elif menu == 4 : # 출금
            print("--------------")
            print("---- 출금 ----")
            print("--------------")
            account_no = input("> 계좌번호")
            amount = int(input("> 출금액 : "))
            aservice.withdraw(account_no, amount)


    print("======= 이용해 주셔서 감사합니다람쥐. =======")

if __name__ == '__main__':
    aservice = AccountService()
    start_console_bank(aservice)