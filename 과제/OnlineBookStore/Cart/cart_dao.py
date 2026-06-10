from Cart.cart import Cart
#====================
# 장바구니 데이터 접근 (CRUD) : CartDAO
class CartDAO:
    def __init__(self):
        self.__cartDB = {}   # Key: member_no, Value: Cart

    def create_cart(self, member_no):
        if member_no not in self.__cartDB:
            self.__cartDB[member_no] = Cart(member_no)

    def get_cart(self, member_no):
        return self.__cartDB.get(member_no, None)

    def update_cart(self, member_no, cart):
        self.__cartDB[member_no] = cart

    def clear_cart(self, member_no):
        if member_no in self.__cartDB:
            self.__cartDB[member_no].clear_cart()

    def remove_cart(self, member_no):
        if member_no in self.__cartDB:
            del self.__cartDB[member_no]
