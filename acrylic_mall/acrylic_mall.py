from Member.member import Member
from Member.member_dao import MemberDAO
from Member.member_service import MemberService
from Product.product import Product
from Product.product_dao import ProductDAO
from Product.product_service import ProductService
from Cart.cart_dao import CartDAO
from Cart.cart_service import CartService
from Order.order import Order
from Order.order_dao import OrderDAO
from Order.order_service import OrderService


class ShoppingMallApp:
    # 비회원 메뉴
    start_menu         = ['종료', '로그인', '회원가입', '견적 계산(조회)']
    # 회원 메뉴
    user_menu          = ['로그아웃', '견적내기', '장바구니 관리', '주문 내역 조회', '내 정보 관리']
    user_cart_menu     = ['뒤로가기', '장바구니 보기', '수량 변경', '장바구니 삭제', '주문하기']
    user_order_menu    = ['뒤로가기', '주문 내역 조회', '주문 취소']
    user_myinfo_menu   = ['뒤로가기', '내 정보 조회', '내 정보 수정']
    user_update_menu   = ['취소', '전화번호 변경', '이메일 변경', '주소 변경']
    # 관리자 메뉴
    admin_menu         = ['로그아웃', '단가/재고 관리', '회원 관리', '주문 관리']
    admin_setting_menu = ['뒤로가기', '현재 단가/재고 보기', '기본단가 변경', '재고 변경']
    admin_member_menu  = ['뒤로가기', '회원 목록', '회원 정보 조회']
    admin_order_menu   = ['뒤로가기', '전체 주문 목록', '배송 상태 변경']

    def __init__(self):
        self.msv = MemberService(MemberDAO())
        self.psv = ProductService(ProductDAO())
        self.csv = CartService(CartDAO())
        self.osv = OrderService(OrderDAO())

        # 아크릴 판 기본 설정 (기본단가 5원/cm², 재고 100장)
        self.psv.init_product(5, 100)

        # 테스트 데이터
        self.msv.join(Member('user1', '123', '이근휘', '01012345678', 'user1@a.com', '경기도 성남시'))
        self.msv.join(Member('user2', '123', '이혜정'))

    def main(self):
        self.show_welcome()
        menu = self.select_menu(ShoppingMallApp.start_menu)
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
            elif menu == 3:
                self.menu_guest_estimate()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')
            menu = self.select_menu(ShoppingMallApp.start_menu)

    def show_welcome(self):
        print('======== 아크릴 판 재단 주문제작 쇼핑몰 ==========')

    def say_goodbye(self):
        print('>> 이용해 주셔서 감사합니다.')

    LINE = '=' * 75

#======================================= 공통 출력/입력 유틸

    # 한글은 터미널에서 2칸, 영문/숫자는 1칸 → 실제 출력 너비 계산
    def str_width(self, s):
        width = 0
        for c in str(s):
            width += 2 if ord(c) > 127 else 1
        return width

    def ljust_k(self, s, width):
        return str(s) + ' ' * (width - self.str_width(s))

    def rjust_k(self, s, width):
        return ' ' * (width - self.str_width(s)) + str(s)

    def center_k(self, s, width):
        pad = width - self.str_width(s)
        left = pad // 2
        return ' ' * left + str(s) + ' ' * (pad - left)

    def select_menu(self, menu_list, skip_top_line=False):
        if not skip_top_line:
            print(ShoppingMallApp.LINE)
        for index in range(1, len(menu_list)):
            print(f'{index}. {menu_list[index]}', end='   ')
        print(f'0. {menu_list[0]}')
        print(ShoppingMallApp.LINE)
        try:
            return int(input('>> 메뉴 : '))
        except ValueError:
            return -1

    def input_positive_int(self, prompt):
        try:
            value = int(input(prompt))
        except ValueError:
            print('>> 숫자를 입력하세요.')
            return None
        if value <= 0:
            print('>> 0보다 큰 값을 입력하세요.')
            return None
        return value

    def input_positive_float(self, prompt):
        try:
            value = float(input(prompt))
        except ValueError:
            print('>> 숫자를 입력하세요.')
            return None
        if value <= 0:
            print('>> 0보다 큰 값을 입력하세요.')
            return None
        return value

    def input_thickness(self):
        options = list(Product.THICKNESS_RATIO.keys())
        thickness = input(f'>> 두께 {options} : ').strip().upper()
        if thickness not in Product.THICKNESS_RATIO:
            print('>> 2T, 3T, 5T, 8T 중에서 선택하세요.')
            return None
        return thickness

    # 색상 선택 (특정 색상만 허용)
    def input_color(self):
        print(f'>> 선택 가능 색상 : {Product.COLORS}')
        color = input('>> 색상 : ').strip()
        if color not in Product.COLORS:
            print(f'>> {Product.COLORS} 중에서 선택하세요.')
            return None
        return color

#======================================= 견적

    def do_estimate(self):
        color = self.input_color()
        if color is None:
            return None
        thickness = self.input_thickness()
        if thickness is None:
            return None
        width = self.input_positive_float('>> 가로(cm) : ')
        if width is None:
            return None
        height = self.input_positive_float('>> 세로(cm) : ')
        if height is None:
            return None
        qty = self.input_positive_int('>> 수량 : ')
        if qty is None:
            return None

        base_price = self.psv.get_base_price()
        amount = Product.calc_price(base_price, width, height, thickness, qty)
        area = width * height
        print(ShoppingMallApp.LINE)
        print(f'옵션 : 색상 {color} / {thickness} / {width}cm x {height}cm / 수량 {qty}개')
        print(f'면적 : {area:.1f}cm²  ×  단가 {base_price}원  ×  두께배율 {Product.THICKNESS_RATIO[thickness]}')
        print(f'견적 금액 : {amount}원')
        print(ShoppingMallApp.LINE)
        return color, thickness, width, height, qty, amount

    # 비회원 견적 (구매 불가)
    def menu_guest_estimate(self):
        print('>>>> 견적 계산 (비회원) <<<<')
        result = self.do_estimate()
        if result:
            print('>> 비회원은 견적만 가능합니다. 구매를 원하시면 로그인 후 이용하세요.')

    def menu_login(self):
        print('>>>>>>>> 로그인 <<<<<<<<')
        id = input('아이디 : ')
        pw = input('비밀번호 : ')
        if self.msv.login(id, pw):
            member = self.msv.view_member_info(id)
            print(f'>> {member.get_name()}님, 환영합니다.')
            if self.msv.is_admin():
                self.run_admin_menu()
            else:
                self.csv.create_cart(member.get_member_no())
                self.run_user_menu()
        else:
            print('>> 로그인 실패 (아이디 또는 비밀번호 불일치)')

    def menu_join(self):
        print('>>>>> 회원가입 <<<<<')
        id      = input('아이디 : ').strip()
        pw      = input('비밀번호 : ').strip()
        name    = input('이름 : ').strip()
        phone   = input('전화번호 : ').strip()
        email   = input('이메일 : ').strip()
        address = input('주소 : ').strip()
        if not id or not pw or not name:
            print('>> 아이디/비밀번호/이름은 필수입니다.')
            return
        if self.msv.join(Member(id, pw, name, phone, email, address)):
            print('>> 회원가입 성공')
        else:
            print('>> 이미 존재하는 아이디입니다.')

#======================================= 회원 (USER)

    def run_user_menu(self):
        while True:
            menu = self.select_menu(ShoppingMallApp.user_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.menu_add_to_cart()
            elif menu == 2:
                self.run_cart_menu()
            elif menu == 3:
                self.run_order_menu()
            elif menu == 4:
                self.run_myinfo_menu()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')
        self.msv.logout()

    def _current_member_no(self):
        return self.msv.view_member_info(self.msv.current_user).get_member_no()

    def menu_add_to_cart(self):
        print('>>>> 견적내기<<<<')
        result = self.do_estimate()
        if not result:
            return
        color, thickness, width, height, qty, amount = result
        if self.psv.get_stock() < qty:
            print(f'>> 재고가 부족합니다. (현재 재고: {self.psv.get_stock()}장)')
            return
        confirm = input('>> 장바구니에 담으시겠습니까? (y/n) : ').strip().lower()
        if confirm != 'y':
            return
        self.csv.add_to_cart(self._current_member_no(), color, thickness, width, height, qty, amount)
        print('>> 장바구니에 담았습니다.')

    def run_cart_menu(self):
        while True:
            # 장바구니 내용을 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_view_cart()
            menu = self.select_menu(ShoppingMallApp.user_cart_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                # 이미 위에서 장바구니를 보여줬으므로 다시 출력하지 않고 메뉴 갱신
                continue
            elif menu == 2:
                self.menu_update_cart_item(show_cart=False)
            elif menu == 3:
                self.menu_delete_cart_item(show_cart=False)
            elif menu == 4:
                self.menu_create_order()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_view_cart(self):
        print('>>>> 장바구니 보기 <<<<')
        cart = self.csv.view_cart(self._current_member_no())
        if not cart or cart.is_empty():
            print('>> 장바구니가 비어 있습니다.')
            print(ShoppingMallApp.LINE)
            return None
        print(ShoppingMallApp.LINE)
        print(self.center_k('항목', 6) + ' | ' + self.center_k('색상', 8) + ' | ' +
              self.center_k('두께', 6) + ' | ' + self.center_k('규격', 16) + ' | ' +
              self.rjust_k('수량', 6) + ' | ' + self.rjust_k('금액', 12))
        print(ShoppingMallApp.LINE)
        for item in cart.get_items():
            print(self.center_k(item.get_item_no(), 6) + ' | ' + self.center_k(item.get_color(), 8) + ' | ' +
                  self.center_k(item.get_thickness(), 6) + ' | ' +
                  self.center_k(f'{item.get_width()}x{item.get_height()}cm', 16) + ' | ' +
                  self.rjust_k(f'{item.get_qty()}개', 6) + ' | ' + self.rjust_k(f'{item.get_amount()}원', 12))
        print(ShoppingMallApp.LINE)
        print(f'>> 총 주문 금액 : {cart.total()}원')
        print(ShoppingMallApp.LINE)
        return cart

    def menu_delete_cart_item(self, show_cart=True):
        print('>>>> 장바구니 삭제 <<<<')
        if show_cart:
            cart = self.menu_view_cart()
        else:
            cart = self.csv.view_cart(self._current_member_no())
        if not cart or cart.is_empty():
            print('>> 장바구니가 비어 있습니다.')
            print(ShoppingMallApp.LINE)
            return
        item_no = self.input_positive_int('>> 삭제할 항목 번호 : ')
        if item_no is None:
            return
        if self.csv.delete_cart_item(self._current_member_no(), item_no):
            print('>> 삭제 성공')
        else:
            print('>> 존재하지 않는 항목 번호입니다.')

    def menu_update_cart_item(self, show_cart=True):
        print('>>>> 수량 변경 <<<<')
        if show_cart:
            cart = self.menu_view_cart()
        else:
            cart = self.csv.view_cart(self._current_member_no())
        if not cart or cart.is_empty():
            print('>> 장바구니가 비어 있습니다.')
            print(ShoppingMallApp.LINE)
            return
        item_no = self.input_positive_int('>> 변경할 항목 번호 : ')
        if item_no is None:
            return
        member_no = self._current_member_no()
        if not cart.get_item(item_no):
            print('>> 존재하지 않는 항목 번호입니다.')
            return
        new_qty = self.input_positive_int('>> 새 수량 : ')
        if new_qty is None:
            return
        if self.psv.get_stock() < new_qty:
            print(f'>> 재고가 부족합니다. (현재 재고: {self.psv.get_stock()}장)')
            return
        if self.csv.update_cart_item_qty(member_no, item_no, new_qty, self.psv.get_base_price()):
            print('>> 수량 변경 성공')
        else:
            print('>> 수량 변경 실패')

    def menu_create_order(self):
        print('>>>> 주문하기 <<<<')
        member_no = self._current_member_no()
        cart = self.csv.view_cart(member_no)
        if not cart or cart.is_empty():
            print('>> 장바구니가 비어 있습니다.')
            return

        # 재고 확인 (전체 수량 합계 기준)
        total_qty = sum(item.get_qty() for item in cart.get_items())
        if self.psv.get_stock() < total_qty:
            print(f'>> 재고가 부족합니다. (필요: {total_qty}장, 재고: {self.psv.get_stock()}장)')
            return

        self.menu_view_cart()
        member = self.msv.view_member_info(self.msv.current_user)
        phone = member.get_phone()
        email = member.get_email()
        default_addr = member.get_address()

        if not phone:
            phone = input('>> 전화번호 : ').strip()

        address = input(f'>> 배송지 [{default_addr}] : ').strip()
        if not address:
            address = default_addr
        if not address:
            print('>> 배송지를 입력해야 합니다.')
            return
        confirm = input('>> 주문하시겠습니까? (y/n) : ').strip().lower()
        if confirm != 'y':
            return

        if phone != member.get_phone() or address != member.get_address():
            self.msv.update_member_info(self.msv.current_user, phone, email, address)

        self.psv.decrease_stock(total_qty)
        order = self.osv.create_order(member_no, cart.get_items(), cart.total(), address)
        self.csv.clear_cart(member_no)
        print(f'>> 주문 완료! 주문번호 {order.get_order_no()}')

    def run_order_menu(self):
        while True:
            # 주문 내역을 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_view_my_orders()
            menu = self.select_menu(ShoppingMallApp.user_order_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                continue
            elif menu == 2:
                self.menu_cancel_order(show_orders=False)
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_view_my_orders(self):
        print('>>>> 주문 내역 조회 <<<<')
        orders = self.osv.view_my_orders(self._current_member_no())
        if not orders:
            print('>> 주문 내역이 없습니다.')
            print(ShoppingMallApp.LINE)
            return
        for order in orders:
            print(ShoppingMallApp.LINE)
            print(order)
            for item in order.get_items():
                print('   - ' + str(item))
        print(ShoppingMallApp.LINE)

    def menu_cancel_order(self, show_orders=True):
        print('>>>> 주문 취소 <<<<')
        member_no = self._current_member_no()
        orders = self.osv.view_my_orders(member_no)
        if not orders:
            print('>> 주문 내역이 없습니다.')
            return
        if show_orders:
            self.menu_view_my_orders()
        order_no = self.input_positive_int('>> 취소할 주문 번호 : ')
        if order_no is None:
            return
        order = self.osv.get_order(order_no)
        if not order or order.get_member_no() != member_no:
            print('>> 존재하지 않는 주문입니다.')
            return
        if order.get_status() != Order.STATUS_ORDERED:
            print(f'>> 취소할 수 없는 주문입니다. (현재 상태: {order.get_status()})')
            return
        confirm = input('>> 정말 취소하시겠습니까? (y/n) : ').strip().lower()
        if confirm != 'y':
            return
        total_qty = sum(item.get_qty() for item in order.get_items())
        if self.osv.cancel_order(order_no, member_no):
            self.psv.increase_stock(total_qty)
            print(f'>> 주문 {order_no} 취소 완료')
        else:
            print('>> 주문 취소 실패')

    def run_myinfo_menu(self):
        while True:
            # 내 정보를 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_view_myinfo()
            menu = self.select_menu(ShoppingMallApp.user_myinfo_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                continue
            elif menu == 2:
                self.menu_update_myinfo()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_view_myinfo(self):
        print(ShoppingMallApp.LINE)
        print(self.msv.view_member_info(self.msv.current_user))
        print(ShoppingMallApp.LINE)

    def menu_update_myinfo(self):
        print('>>>> 내 정보 수정 <<<<')
        member = self.msv.view_member_info(self.msv.current_user)
        menu = self.select_menu(ShoppingMallApp.user_update_menu)
        phone, email, address = member.get_phone(), member.get_email(), member.get_address()
        if menu == 1:
            phone = input(f'>> 새 전화번호 [{phone}] : ').strip() or phone
        elif menu == 2:
            email = input(f'>> 새 이메일 [{email}] : ').strip() or email
        elif menu == 3:
            address = input(f'>> 새 주소 [{address}] : ').strip() or address
        else:
            return
        self.msv.update_member_info(self.msv.current_user, phone, email, address)
        print('>> 정보 수정 성공')

#======================================= 관리자 (ADMIN)

    def run_admin_menu(self):
        while True:
            menu = self.select_menu(ShoppingMallApp.admin_menu)
            if menu == 0:
                break
            elif menu == 1:
                self.run_admin_setting_menu()
            elif menu == 2:
                self.run_admin_member_menu()
            elif menu == 3:
                self.run_admin_order_menu()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')
        self.msv.logout()

    def run_admin_setting_menu(self):
        while True:
            # 현재 단가/재고를 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_show_setting()
            menu = self.select_menu(ShoppingMallApp.admin_setting_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                continue
            elif menu == 2:
                self.menu_change_price()
            elif menu == 3:
                self.menu_change_stock()
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_show_setting(self):
        print(ShoppingMallApp.LINE)
        print(self.psv.get_product())
        print(ShoppingMallApp.LINE)

    def menu_change_price(self):
        print('>>>> 기본단가 변경 <<<<')
        price = self.input_positive_int(f'>> 새 기본단가(cm²당 원) [{self.psv.get_base_price()}] : ')
        if price is None:
            return
        self.psv.set_base_price(price)
        print('>> 기본단가 변경 성공')

    def menu_change_stock(self):
        print('>>>> 재고 변경 <<<<')
        stock = self.input_positive_int(f'>> 새 재고(장) [{self.psv.get_stock()}] : ')
        if stock is None:
            return
        self.psv.set_stock(stock)
        print('>> 재고 변경 성공')

    def run_admin_member_menu(self):
        while True:
            # 회원 목록을 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_list_members()
            menu = self.select_menu(ShoppingMallApp.admin_member_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                continue
            elif menu == 2:
                self.menu_view_member_detail(show_list=False)
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_list_members(self):
        print('>>>> 회원 목록 <<<<')
        members = [m for m in self.msv.list_members() if m.get_id() != MemberService.ADMIN_ID]
        if not members:
            print('>> 등록된 회원이 없습니다.')
            print(ShoppingMallApp.LINE)
            return
        print(ShoppingMallApp.LINE)
        for m in members:
            print(m)
        print(ShoppingMallApp.LINE)

    def menu_view_member_detail(self, show_list=True):
        print('>>>> 회원 정보 조회 <<<<')
        if show_list:
            self.menu_list_members()
        id = input('>> 조회할 회원 아이디 : ').strip()
        member = self.msv.view_member_info(id)
        if member and id != MemberService.ADMIN_ID:
            print(ShoppingMallApp.LINE)
            print(member)
            print(ShoppingMallApp.LINE)
        else:
            print('>> 회원이 존재하지 않습니다.')

    def run_admin_order_menu(self):
        while True:
            # 전체 주문 목록을 먼저 보여주고, 바로 아래에 메뉴를 한 줄 구분선으로 출력
            self.menu_list_all_orders()
            menu = self.select_menu(ShoppingMallApp.admin_order_menu, skip_top_line=True)
            if menu == 0:
                break
            elif menu == 1:
                continue
            elif menu == 2:
                self.menu_update_order_status(show_orders=False)
            else:
                print('>> 잘못된 메뉴입니다. 다시 선택하세요.')

    def menu_list_all_orders(self):
        print('>>>> 전체 주문 목록 <<<<')
        orders = self.osv.view_all_orders()
        if not orders:
            print('>> 주문이 없습니다.')
            print(ShoppingMallApp.LINE)
            return None
        for order in orders:
            print(ShoppingMallApp.LINE)
            print(order)
            for item in order.get_items():
                print('   - ' + str(item))
        print(ShoppingMallApp.LINE)
        return orders

    def menu_update_order_status(self, show_orders=True):
        print('>>>> 배송 상태 변경 <<<<')
        if show_orders and not self.menu_list_all_orders():
            return
        if not show_orders and not self.osv.view_all_orders():
            print('>> 주문이 없습니다.')
            return
        order_no = self.input_positive_int('>> 변경할 주문 번호 : ')
        if order_no is None:
            return
        order = self.osv.get_order(order_no)
        if not order:
            print('>> 존재하지 않는 주문입니다.')
            return
        if order.get_status() == Order.STATUS_CANCELLED:
            print('>> 취소된 주문은 변경할 수 없습니다.')
            return
        print(f'1. {Order.STATUS_SHIPPING}   2. {Order.STATUS_DONE}')
        choice = input('>> 상태 선택 : ').strip()
        if choice == '1':
            status = Order.STATUS_SHIPPING
        elif choice == '2':
            status = Order.STATUS_DONE
        else:
            print('>> 잘못된 입력입니다.')
            return
        if self.osv.update_status(order_no, status):
            print('>> 상태 변경 성공')
        else:
            print('>> 상태 변경 실패')



if __name__ == '__main__':
    app = ShoppingMallApp()
    app.main()
