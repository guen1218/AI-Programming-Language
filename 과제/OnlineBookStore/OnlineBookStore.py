from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Book.book import Book
from Book.book_dao import BookDAO
from Book.book_service import BookService
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order_dao import OrderDAO
from Order.order_service import OrderService
from Order.order import Order
from Delivery.delivery_dao import DeliveryDAO
from Delivery.delivery_service import DeliveryService

class BookShopApp:
    start_menu        = ['종료', '로그인', '회원가입']
    user_menu         = ['로그아웃', '장바구니 관리', '주문하기', '주문/배송 조회', '내 정보 관리']
    user_cart_menu    = ['뒤로가기', '장바구니 담기', '장바구니 보기', '장바구니 삭제', '주문하기']
    user_order_menu   = ['뒤로가기', '내 주문 내역', '주문 취소', '내 배송 조회']
    user_myinfo_menu  = ['뒤로가기', '내 정보 조회', '내 정보 수정', '회원 탈퇴']
    user_update_menu  = ['취소', '이름 변경', '비밀번호 변경', '전화번호 변경', '주소 변경']
    admin_menu        = ['로그아웃', '도서 관리 메뉴', '회원 관리 메뉴', '주문 관리 메뉴', '배송 관리 메뉴']
    admin_book_menu      = ['뒤로가기', '도서 목록', '도서 등록', '도서 수정', '도서 삭제']
    admin_edit_book_menu = ['취소', '제목 변경', '저자 변경', '출판사 변경', '가격 변경', '재고 변경']
    admin_member_menu = ['뒤로가기', '회원 목록', '회원 정보 조회', '회원 강퇴']
    admin_order_menu  = ['뒤로가기', '전체 주문 목록', '주문 거부']
    admin_deli_menu   = ['뒤로가기', '전체 배송 조회', '배송 상태 수정']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.bsv = BookService(BookDAO())
        self.csv = CartService(CartDAO())
        order_dao = OrderDAO()
        self.osv = OrderService(order_dao)
        self.dsv = DeliveryService(DeliveryDAO(order_dao), self.osv, self.msv)

        # 테스트 데이터
        self.msv.join(Member('user1', '1234', '이유찬', '01012345678', '지옥'))
        self.msv.join(Member('user2', '1234', '전만수'))
        self.msv.join(Member('user3', '1234', '박만욱'))
        self.bsv.add_book('벨 푸페의 슈퍼달링 약혼', '아사기리 아사키', '학산문화사', 10000, 15)
        self.bsv.add_book('패배 히로인이 너무 많아!', '아마모리 타키비', '디앤씨미디어', 9000, 12)
        self.bsv.add_book('Re: 제로부터 시작하는 이세계 생활', '나가츠키 탓페이', '노블엔진', 7200, 10)
        self.bsv.add_book('마녀의 여행', '시라이시 조우기', '소미미디어', 9500, 8)
        self.bsv.add_book('전생했더니 슬라임이었던 건에 대하여', '후세', '소미미디어', 10000, 5)
        self.bsv.add_book('사일런트 위치', '이소라 마츠리', 'S노벨플러스', 9000, 7)

    def main(self):
        self.show_welcome()
        self.menu_show_books()
        menu = self.select_menu(BookShopApp.start_menu)
        self.run_start_menu(menu)
        self.say_goodbye()

    def run_start_menu(self, menu):
        while True:
            if menu == 0:
                break
            elif menu == 1:
                self.menu_login()
            elif menu == 2:
                self.menu_join()
            else:
                print('다시하시오')
            menu = self.select_menu(BookShopApp.start_menu)

    def show_welcome(self):
        print('======== Online Book Store ==========')

    def say_goodbye(self):
        print('>> 온라인 서점을 이용해 주셔서 감사합니다.')

    LINE = '=' * 90

    # 한글은 터미널에서 2칸, 영문/숫자는 1칸 → 실제 출력 너비 계산
    def str_width(self, s):
        width = 0
        for c in str(s):
            if ord(c) > 127:
                width += 2
            else:
                width += 1
        return width

    # 왼쪽 정렬: 실제 너비 기준으로 공백 채움
    def ljust_k(self, s, width):
        return str(s) + ' ' * (width - self.str_width(s))

    # 오른쪽 정렬: 실제 너비 기준으로 공백 채움
    def rjust_k(self, s, width):
        return ' ' * (width - self.str_width(s)) + str(s)

    # 가운데 정렬
    def center_k(self, s, width):
        pad = width - self.str_width(s)
        left = pad // 2
        right = pad - left
        return ' ' * left + str(s) + ' ' * right

    def select_menu(self, menu_list):
        print(BookShopApp.LINE)
        for index in range(1, len(menu_list)):
            print(f'{index}. {menu_list[index]}', end='   ')
        print(f'0. {menu_list[0]}')
        print(BookShopApp.LINE)
        try:
            num = int(input('>> 메뉴 : '))
        except ValueError:
            return -1
        else:
            return num

    def menu_login(self):
        print('>>>>>>>> 로그인 <<<<<<<<<')
        id = input('아이디 : ')
        pw = input('비밀번호 : ')
        if self.msv.login(id, pw):
            print(f'{self.msv.view_member_info(id).get_name()}님, 환영합니다.')
            member_no = self.msv.view_member_info(id).get_member_no()
            self.csv.create_cart(member_no)
            if self.msv.current_user == MemberService.ADMIN_ID:
                self.run_admin_menu()
            else:
                self.run_user_menu()
        else:
            print('로그인 실패')

    def menu_join(self):
        print('>>>>> 회원가입 <<<<<')
        name = input('이름 : ')
        id   = input('아이디 : ')
        pw   = input('비밀번호 : ')
        if self.msv.join(Member(id, pw, name)):
            print('회원가입 성공')
        else:
            print('회원가입 실패')

    def menu_show_books(self):
        print('>>>>도서 목록<<<<')
        books = self.bsv.show_books()
        if not books:
            print('등록된 도서가 없습니다')
            return
        print(BookShopApp.LINE)
        print(self.center_k('번호', 6) + ' | ' + self.ljust_k('제목', 36) + ' | ' + self.ljust_k('저자', 16) + ' | ' + self.rjust_k('가격', 10) + ' | ' + self.rjust_k('재고', 6))
        print(BookShopApp.LINE)
        for book in books:
            print(self.center_k(book.get_book_no(), 6) + ' | ' + self.ljust_k(book.get_title(), 36) + ' | ' + self.ljust_k(book.get_author(), 16) + ' | ' + self.rjust_k(str(book.get_price()) + '원', 10) + ' | ' + self.rjust_k(str(book.get_stock()) + '권', 6))
        print(BookShopApp.LINE)

#======================================= user

    def run_user_menu(self):
        while True:
            self.menu_show_books()
            menu = self.select_menu(BookShopApp.user_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.run_cart_menu()
            elif menu == 2:
                self.menu_create_order()
            elif menu == 3:
                self.run_order_menu()
            elif menu == 4:
                if self.run_myinfo_menu() == 'backhome':
                    break
            else:
                print('다시하시오')
        self.msv.current_user = None

    def run_cart_menu(self):
        print('>>>>장바구니 관리<<<<')
        while True:
            menu = self.select_menu(BookShopApp.user_cart_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_add_to_cart()
            elif menu == 2:
                self.menu_view_cart()
            elif menu == 3:
                self.menu_delete_cart_item()
            elif menu == 4:
                self.menu_create_order()
            else:
                print('다시하시오')

    def run_order_menu(self):
        print('>>>>주문/배송 조회<<<<')
        while True:
            menu = self.select_menu(BookShopApp.user_order_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_view_my_orders()
            elif menu == 2:
                self.menu_cancel_order()
            elif menu == 3:
                self.menu_view_my_delivery()
            else:
                print('다시하시오')

#======================run_user_menu========================================= ↓

    def menu_add_to_cart(self):
        print('>>>>장바구니 담기<<<<')
        self.menu_show_books()
        try:
            book_no = int(input('>> 도서 번호 : '))
            qty     = int(input('>> 수량 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        book = self.bsv.detail_book(book_no)
        if not book:
            print('존재하지 않는 도서입니다')
            return
        cart = self.csv.view_cart(self._current_member_no())
        already_in_cart = 0
        if cart and book_no in cart.get_items():
            already_in_cart = cart.get_items()[book_no]
        if book.get_stock() < already_in_cart + qty:
            print(f'재고가 부족합니다 (재고: {book.get_stock()}권, 이미 담긴 수량: {already_in_cart}권)')
            return
        self.csv.add_to_cart(self._current_member_no(), book_no, qty)
        print('장바구니에 담았습니다')

    def menu_view_cart(self):
        print('>>>>장바구니 보기<<<<')
        cart = self.csv.view_cart(self._current_member_no())
        if not cart or cart.is_empty():
            print('장바구니가 비어 있습니다')
            return cart
        print(BookShopApp.LINE)
        total = 0
        for book_no, qty in cart.get_items().items():
            book = self.bsv.detail_book(book_no)
            if book:
                subtotal = book.get_price() * qty
                total += subtotal
                print(f'[{book_no}] {book.get_title()} x{qty} = {subtotal}원')
        print(f'합계 : {total}원')
        print(BookShopApp.LINE)
        return cart

    def menu_delete_cart_item(self):
        print('>>>>장바구니 삭제<<<<')
        if not self.menu_view_cart():
            return
        try:
            book_no = int(input('>> 삭제할 도서 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        if self.csv.delete_cart_item(self._current_member_no(), book_no):
            print('삭제 성공')
        else:
            print('삭제 실패')

    def menu_create_order(self):
        print('>>>>주문하기<<<<')
        member_no = self._current_member_no()

        # 전화번호/주소 없으면 먼저 입력받기
        member = self.msv.view_member_info(self.msv.current_user)
        if not member.get_phone() or not member.get_address():
            print('>> 주문을 위해 연락처 정보가 필요합니다.')
            phone   = input('>> 전화번호 : ')
            address = input('>> 주소 : ')
            member.update_info(member.get_name(), phone, address)
            self.msv.update_member_info(self.msv.current_user, member)

        cart = self.csv.view_cart(member_no)
        if not cart or cart.is_empty():
            print('>> 장바구니가 비어 있습니다. 도서를 직접 선택해 주문합니다.')
            self.menu_show_books()
            try:
                book_no = int(input('>> 주문할 도서 번호 : '))
                qty     = int(input('>> 수량 : '))
            except ValueError:
                print('올바른 숫자를 입력하세요')
                return
            book = self.bsv.detail_book(book_no)
            if not book:
                print('존재하지 않는 도서입니다')
                return
            if book.get_stock() < qty:
                print('재고가 부족합니다')
                return
            order_items = {book_no: qty}
            total = book.get_price() * qty
            print(BookShopApp.LINE)
            print(f'{book.get_title()} x{qty}')
            print(f'총 결제 금액 : {total}원')
            print(BookShopApp.LINE)
            confirm = input('주문하시겠습니까? (y/n) : ').strip()
            if confirm.lower() != 'y':
                return
            self.bsv.decrease_stock(book_no, qty)
            self.osv.create_order(member_no, order_items, total)
            print('주문 완료')
            return
        total = 0
        order_items = {}
        for book_no, qty in cart.get_items().items():
            book = self.bsv.detail_book(book_no)
            if not book or book.get_stock() < qty:
                if book:
                    print(f'재고 부족 : {book.get_title()}')
                else:
                    print(f'재고 부족 : {book_no}')
                return
            total += book.get_price() * qty
            order_items[book_no] = qty
        print(BookShopApp.LINE)
        for book_no, qty in order_items.items():
            book = self.bsv.detail_book(book_no)
            print(f'{book.get_title()} x{qty}')
        print(f'총 결제 금액 : {total}원')
        print(BookShopApp.LINE)
        confirm = input('주문하시겠습니까? (y/n) : ').strip()
        if confirm.lower() != 'y':
            return
        for book_no, qty in order_items.items():
            self.bsv.decrease_stock(book_no, qty)
        self.osv.create_order(member_no, order_items, total)
        self.csv.clear_cart(member_no)
        print('주문 완료')

    def menu_view_my_orders(self):
        print('>>>>내 주문 내역<<<<')
        orders = self.osv.view_my_orders(self._current_member_no())
        if orders:
            print(BookShopApp.LINE)
            for order in orders:
                print(order)
            print(BookShopApp.LINE)
        else:
            print('주문 내역이 없습니다')
        return orders

    def menu_cancel_order(self):
        print('>>>>주문 취소<<<<')
        if not self.menu_view_my_orders():
            return
        try:
            order_no = int(input('>> 취소할 주문 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        order = self.osv.get_order(order_no)
        if self.osv.cancel_order(order_no, self._current_member_no()):
            for book_no, qty in order.get_order_items().items():
                self.bsv.increase_stock(book_no, qty)
            print('주문 취소 성공')
        else:
            print('주문 취소 실패 (취소 가능한 상태가 아닙니다)')

    def menu_view_my_delivery(self):
        print('>>>>내 배송 조회<<<<')
        deliveries = self.dsv.view_my_delivery(self._current_member_no())
        if deliveries:
            print(BookShopApp.LINE)
            for d in deliveries:
                print(d)
            print(BookShopApp.LINE)
        else:
            print('배송 정보가 없습니다')

#======================run_user_menu========================================= ↑

    def run_myinfo_menu(self):
        self.menu_view_myinfo()
        while True:
            menu = self.select_menu(BookShopApp.user_myinfo_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_view_myinfo()
            elif menu == 2:
                self.menu_update_myinfo()
            elif menu == 3:
                if self.menu_withdraw() == 'backhome':
                    return 'backhome'
            else:
                print('다시하시오')

    def menu_view_myinfo(self):
        print(BookShopApp.LINE)
        print(self.msv.view_member_info(self.msv.current_user))
        print(BookShopApp.LINE)

    def menu_update_myinfo(self):
        print('>>>>내 정보 수정<<<<')
        self.menu_view_myinfo()
        menu = self.select_menu(BookShopApp.user_update_menu)
        if menu == 1:
            self.menu_update_name()
        elif menu == 2:
            self.menu_update_password()
        elif menu == 3:
            self.menu_update_phone()
        elif menu == 4:
            self.menu_update_address()

    def menu_update_name(self):
        print('>>>>이름 변경<<<<')
        member = self.msv.view_member_info(self.msv.current_user)
        name = input(f'>> 새 이름 [{member.get_name()}] : ').strip()
        if not name:
            print('이름을 입력하세요')
            return
        member.update_info(name, member.get_phone(), member.get_address())
        self.msv.update_member_info(self.msv.current_user, member)
        print('이름 변경 성공')

    def menu_update_password(self):
        print('>>>>비밀번호 변경<<<<')
        member = self.msv.view_member_info(self.msv.current_user)
        org_pw = input('>> 현재 비밀번호 : ').strip()
        if not member.check_password(org_pw):
            print('현재 비밀번호가 틀렸습니다')
            return
        new_pw = input('>> 새 비밀번호 : ').strip()
        if not new_pw:
            print('비밀번호를 입력하세요')
            return
        member.set_password(new_pw)
        self.msv.update_member_info(self.msv.current_user, member)
        print('비밀번호 변경 성공')

    def menu_update_phone(self):
        print('>>>>전화번호 변경<<<<')
        member = self.msv.view_member_info(self.msv.current_user)
        phone = input(f'>> 새 전화번호 [{member.get_phone()}] : ').strip()
        if not phone:
            print('전화번호를 입력하세요')
            return
        member.update_info(member.get_name(), phone, member.get_address())
        self.msv.update_member_info(self.msv.current_user, member)
        print('전화번호 변경 성공')

    def menu_update_address(self):
        print('>>>>주소 변경<<<<')
        member = self.msv.view_member_info(self.msv.current_user)
        address = input(f'>> 새 주소 [{member.get_address()}] : ').strip()
        if not address:
            print('주소를 입력하세요')
            return
        member.update_info(member.get_name(), member.get_phone(), address)
        self.msv.update_member_info(self.msv.current_user, member)
        print('주소 변경 성공')

    def menu_withdraw(self):
        print('>>>>회원 탈퇴<<<<')
        pw = input('>> 비밀번호 확인 : ')
        member = self.msv.view_member_info(self.msv.current_user)
        if member.check_password(pw):
            self.csv.clear_cart(member.get_member_no())
            self.msv.remove_member(self.msv.current_user)
            print('탈퇴 성공')
            return 'backhome'
        print('비밀번호가 틀렸습니다')

    def _current_member_no(self):
        return self.msv.view_member_info(self.msv.current_user).get_member_no()

#======================================= user


#======================================= admin

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(BookShopApp.admin_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.run_admin_book_menu()
            elif menu == 2:
                self.run_admin_member_menu()
            elif menu == 3:
                self.run_admin_order_menu()
            elif menu == 4:
                self.run_admin_deli_menu()
            else:
                print('다시하시오')
        self.msv.current_user = None

#========================================

    def run_admin_book_menu(self):
        print('>>>>도서 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(BookShopApp.admin_book_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_show_books()
            elif menu == 2:
                self.menu_add_book()
            elif menu == 3:
                self.menu_edit_book()
            elif menu == 4:
                self.menu_delete_book()
            else:
                print('다시하시오')

    def menu_add_book(self):
        print('>>>>도서 등록<<<<')
        title     = input('제목 : ')
        author    = input('저자 : ')
        publisher = input('출판사 : ')
        try:
            price = int(input('가격 : '))
            stock = int(input('재고 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        self.bsv.add_book(title, author, publisher, price, stock)
        print('도서 등록 성공')

    def menu_edit_book(self):
        print('>>>>도서 수정<<<<')
        self.menu_show_books()
        try:
            book_no = int(input('>> 수정할 도서 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        book = self.bsv.detail_book(book_no)
        if not book:
            print('존재하지 않는 도서입니다')
            return
        menu = self.select_menu(BookShopApp.admin_edit_book_menu)
        if menu == 1:
            self.menu_edit_book_title(book_no, book)
        elif menu == 2:
            self.menu_edit_book_author(book_no, book)
        elif menu == 3:
            self.menu_edit_book_publisher(book_no, book)
        elif menu == 4:
            self.menu_edit_book_price(book_no, book)
        elif menu == 5:
            self.menu_edit_book_stock(book_no, book)

    def menu_edit_book_title(self, book_no, book):
        print('>>>>제목 변경<<<<')
        title = input(f'>> 새 제목 [{book.get_title()}] : ').strip()
        if not title:
            print('제목을 입력하세요')
            return
        self.bsv.edit_book(book_no, title, book.get_author(), book.get_publisher(), book.get_price())
        print('제목 변경 성공')

    def menu_edit_book_author(self, book_no, book):
        print('>>>>저자 변경<<<<')
        author = input(f'>> 새 저자 [{book.get_author()}] : ').strip()
        if not author:
            print('저자를 입력하세요')
            return
        self.bsv.edit_book(book_no, book.get_title(), author, book.get_publisher(), book.get_price())
        print('저자 변경 성공')

    def menu_edit_book_publisher(self, book_no, book):
        print('>>>>출판사 변경<<<<')
        publisher = input(f'>> 새 출판사 [{book.get_publisher()}] : ').strip()
        if not publisher:
            print('출판사를 입력하세요')
            return
        self.bsv.edit_book(book_no, book.get_title(), book.get_author(), publisher, book.get_price())
        print('출판사 변경 성공')

    def menu_edit_book_price(self, book_no, book):
        print('>>>>가격 변경<<<<')
        try:
            price = int(input(f'>> 새 가격 [{book.get_price()}] : ').strip())
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        self.bsv.edit_book(book_no, book.get_title(), book.get_author(), book.get_publisher(), price)
        print('가격 변경 성공')

    def menu_edit_book_stock(self, book_no, book):
        print('>>>>재고 변경<<<<')
        try:
            stock = int(input(f'>> 새 재고 [{book.get_stock()}] : ').strip())
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        self.bsv.update_stock(book_no, stock)
        print('재고 변경 성공')

    def menu_delete_book(self):
        print('>>>>도서 삭제<<<<')
        self.menu_show_books()
        try:
            book_no = int(input('>> 삭제할 도서 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        if self.bsv.delete_book(book_no):
            print('삭제 성공')
        else:
            print('삭제 실패')

#========================================

    def run_admin_member_menu(self):
        print('>>>>회원 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(BookShopApp.admin_member_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_members()
            elif menu == 2:
                self.menu_view_member_info()
            elif menu == 3:
                self.menu_kick_member()
            else:
                print('다시하시오')

    def menu_list_members(self):
        print('>>>>회원 목록<<<<')
        members = self.msv.list_members()
        mem_list = []
        if members:
            for m in members:
                if m.get_id() != MemberService.ADMIN_ID:
                    mem_list.append(m)
        if mem_list:
            print(BookShopApp.LINE)
            for m in mem_list:
                print(m)
            print(BookShopApp.LINE)
        else:
            print('등록된 회원이 없습니다')
        return mem_list

    def menu_view_member_info(self):
        print('>>>>회원 정보 조회<<<<')
        self.menu_list_members()
        id = input('>> 조회할 회원 아이디 : ')
        member = self.msv.view_member_info(id)
        if member:
            print(BookShopApp.LINE)
            print(member)
            print(BookShopApp.LINE)
            return
        print('회원이 존재하지 않습니다')

    def menu_kick_member(self):
        print('>>>>회원 강퇴<<<<')
        self.menu_list_members()
        id = input('>> 강퇴할 회원 아이디 : ')
        if id == MemberService.ADMIN_ID:
            print('관리자는 강퇴할 수 없습니다')
            return
        if self.msv.view_member_info(id):
            self.msv.remove_member(id)
            print('강퇴 성공')
            return
        print('강퇴 실패')

#========================================

    def run_admin_order_menu(self):
        print('>>>>주문 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(BookShopApp.admin_order_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_all_orders()
            elif menu == 2:
                self.menu_reject_order()
            else:
                print('다시하시오')

    def menu_list_all_orders(self):
        print('>>>>전체 주문 목록<<<<')
        orders = self.osv.view_all_orders()
        if orders:
            print(BookShopApp.LINE)
            for order in orders:
                print(order)
            print(BookShopApp.LINE)
        else:
            print('주문이 없습니다')
        return orders

    def menu_reject_order(self):
        print('>>>>주문 거부<<<<')
        if not self.menu_list_all_orders():
            return
        try:
            order_no = int(input('>> 거부할 주문 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        order = self.osv.get_order(order_no)
        if not order:
            print('존재하지 않는 주문입니다')
            return
        if order.get_order_status() == Order.STATUS_CANCELLED:
            print('이미 취소된 주문은 거부할 수 없습니다')
            return
        if order.get_order_status() == Order.STATUS_REJECTED:
            print('이미 거부된 주문입니다')
            return
        if self.osv.reject_order(order_no):
            for book_no, qty in order.get_order_items().items():
                self.bsv.increase_stock(book_no, qty)
            print('주문 거부 성공')
        else:
            print('주문 거부 실패')

#========================================

    def run_admin_deli_menu(self):
        print('>>>>배송 관리 메뉴<<<<')
        while True:
            menu = self.select_menu(BookShopApp.admin_deli_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_list_all_deliveries()
            elif menu == 2:
                self.menu_update_delivery_status()
            else:
                print('다시하시오')

    def menu_list_all_deliveries(self):
        print('>>>>전체 배송 조회<<<<')
        deliveries = self.dsv.view_all_deliveries()
        if deliveries:
            print(BookShopApp.LINE)
            for d in deliveries:
                print(d)
            print(BookShopApp.LINE)
        else:
            print('배송 정보가 없습니다')
        return deliveries

    def menu_update_delivery_status(self):
        print('>>>>배송 상태 수정<<<<')
        if not self.menu_list_all_deliveries():
            return
        try:
            order_no = int(input('>> 수정할 주문 번호 : '))
        except ValueError:
            print('올바른 숫자를 입력하세요')
            return
        order = self.osv.get_order(order_no)
        if not order:
            print('존재하지 않는 주문입니다')
            return
        if order.get_order_status() in (Order.STATUS_CANCELLED, Order.STATUS_REJECTED):
            print('취소/거부된 주문은 배송 상태를 수정할 수 없습니다')
            return
        print(f'1. {Order.STATUS_SHIPPING}   2. {Order.STATUS_DONE}')
        choice = input('>> 상태 선택 : ').strip()
        if choice == '1':
            status = Order.STATUS_SHIPPING
        elif choice == '2':
            status = Order.STATUS_DONE
        else:
            print('잘못된 입력입니다')
            return
        if self.dsv.update_delivery_status(order_no, status):
            print('수정 성공')
        else:
            print('수정 실패')

#======================================= admin

if __name__ == '__main__':
    app = BookShopApp()
    app.main()
