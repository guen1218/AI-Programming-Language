from Cart.cart_dao import CartDAO
#==================
# 장바구니 관리 서비스 로직 : CartService (CART-001 ~ CART-003)
class CartService:
    def __init__(self, cartDao):
        self.__dao = cartDao

    # 회원 장바구니 생성 (로그인 시 호출)
    def create_cart(self, member_no):
        self.__dao.create_cart(member_no)
    def add_to_cart(self, member_no, book_no, qty):
        cart = self.__dao.get_cart(member_no)
        if not cart:
            return False
        cart.add_book(book_no, qty)
        return True
    def view_cart(self, member_no):
        return self.__dao.get_cart(member_no)
    def delete_cart_item(self, member_no, book_no):
        cart = self.__dao.get_cart(member_no)
        if not cart:
            return False
        return cart.remove_book(book_no)

    # 장바구니 전체 비우기 (주문 완료 / 회원 탈퇴 시 호출)
    def clear_cart(self, member_no):
        self.__dao.clear_cart(member_no)
