from member import Member, MemberDAO, MemberService

class MemberManager:
    start_menu = ['종료', '로그인', '회원가입']
    admin_menu = ['로그아웃', '회원목록', '회원정보조회', '회원수정', '회원강퇴']
    member_menu = ['로그아웃', '내정보조회', '내정보수정', '회원탈퇴']
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '1234'

    def __init__(self):
        self.current_user = None
        self.ms = MemberService(MemberDAO())

    def main(self):
        self.show_welcome()
        self.ms.join(Member(MemberManager.ADMIN_ID, MemberManager.ADMIN_PASSWORD, None))
        while True:
            menu = self.select_menu(MemberManager.start_menu)
            if menu == 0: break
            elif menu == 1: # 로그인
                id = input('>> id : ')
                password = input('>> password : ')
                self.current_user = self.ms.login(id, password)
                if self.current_user:
                    if self.current_user == MemberManager.ADMIN_ID:
                        self.start_admin_menu()
                    else:
                        self.start_member_menu()
                else:
                    print('로그인에 실패하였습니다.')

            elif menu == 2: # 회원가입
                id = input('>> id : ')
                password = input('>> password : ')
                name = input('>> name : ')
                member = Member(id, password, name)
                if self.ms.join(member):
                    print('회원가입이 완료되었습니다.')
                else:
                    print('회원가입에 실패하였습니다.')
            else:
                print('없는 메뉴입니다.')
        self.say_goodbye()






#==================어드민=========================

    def start_admin_menu(self):
        print('---------- 관리자 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.admin_menu)
            if menu == 0: break
            elif menu == 1: # 회원목록
                self.list_all_member()
            elif menu == 2: # 회원정보조회
                self.list_member()
            elif menu == 3: # 회원수정
                self.update_member()
            elif menu == 4: # 회원강퇴
                self.remove_member()
            else:
                print('없는 메뉴입니다.')

#==============어드민=============================





#================멤버===========================

    def start_member_menu(self):
        print('---------- 회원 메뉴 ----------')
        while True:
            menu = self.select_menu(MemberManager.member_menu)
            if menu == 0: break
            elif menu == 1: # 내정보조회
                print("미구현")
            elif menu == 2: # 내정보수정
                print("미구현")
            elif menu == 3: # 회원탈퇴
                print("미구현")
            else:
                print('없는 메뉴입니다.')

#=================멤버=========================


    def remove_member(self):
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        input_id = input("없앨 멤버의 id를 입력하시오 : ")
        if self.ms.remove_member(input_id):
            print('삭제 성공')
        else:    
            print('삭제 실패')
    def update_member(self):
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        
        input_id = input("조회할 멤버의 id를 입력하시오 : ")
        member = self.ms.update_member_info(input_id, 1) # member?
        if member:
            print('수정 성공')
        else:    
            print('수정 실패')

    def list_all_member(self):
        print(self.current_user)
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        
        member_list = self.ms.list_members()
        if len(member_list) <= 1:
            print('가입한 회원이 없습니다.')
        else:
            for member in member_list[1:]:
                print(member)

    def list_member(self):
        if self.current_user != MemberManager.ADMIN_ID:
            print('사용 권한이 없습니다.')
            return
        
        input_id = input("조회할 멤버의 id를 입력하시오 : ")
        member = self.ms.list_member_info(input_id)
        if member == None:
            print('해당 사용자는 존재하지 않습니다')
            return
        print(member)

    def show_welcome(self):
        print('=' * 50)
        title = 'Member Manager'
        print(f'{title:^50}')
        print('=' * 50)

    def say_goodbye(self):
        print('안녕히 가세요')

    def print_menu(self, menu_list):
        print('-' * 40)
        for i in range(1, len(menu_list)):
            print(f'{i}. {menu_list[i]}')
        print(f'0. {menu_list[0]}')
        print('-' * 40)

    def select_menu(self, menu_list):
        self.print_menu(menu_list)
        try:
            menu = int(input('메뉴 선택 : '))
            return menu
        except ValueError:
            return -1

if __name__ == '__main__':
    app = MemberManager()
    app.main()