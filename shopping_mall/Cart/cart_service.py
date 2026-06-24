from Cart.cart_dao import CartDAO
from Cart.cart_item import CartItem
from Product.product import Product
#==================
# 장바구니 서비스 로직 : CartService
class CartService:
    def __init__(self, cartDao):
        self.__dao = cartDao

    def create_cart(self, member_no):
        return self.__dao.create_cart(member_no)

    def add_to_cart(self, member_no, color, thickness, width, height, qty, amount):
        cart = self.__dao.create_cart(member_no)
        item = CartItem(color, thickness, width, height, qty, amount)
        cart.add_item(item)
        return True

    def view_cart(self, member_no):
        return self.__dao.get_cart(member_no)

    def delete_cart_item(self, member_no, item_no):
        cart = self.__dao.get_cart(member_no)
        if not cart:
            return False
        return cart.remove_item(item_no)

    def update_cart_item_qty(self, member_no, item_no, new_qty, base_price):
        cart = self.__dao.get_cart(member_no)
        if not cart:
            return False
        item = cart.get_item(item_no)
        if not item:
            return False
        new_amount = Product.calc_price(base_price, item.get_width(), item.get_height(),
                                        item.get_thickness(), new_qty)
        item.set_qty(new_qty)
        item.set_amount(new_amount)
        return True

    def clear_cart(self, member_no):
        cart = self.__dao.get_cart(member_no)
        if cart:
            cart.clear()
