#======================
# 데이터 모델 정의 : CartItem (주문제작 옵션이 적용된 한 항목)
class CartItem:
    def __init__(self, color, thickness, width, height, qty, amount):
        self.__item_no = 0
        self.__color = color
        self.__thickness = thickness
        self.__width = width
        self.__height = height
        self.__qty = qty
        self.__amount = amount   # 견적 금액

    def get_item_no(self):
        return self.__item_no
    def get_color(self):
        return self.__color
    def get_thickness(self):
        return self.__thickness
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    def get_qty(self):
        return self.__qty
    def get_amount(self):
        return self.__amount

    def set_item_no(self, item_no):
        self.__item_no = item_no

    def set_qty(self, qty):
        self.__qty = qty
    def set_amount(self, amount):
        self.__amount = amount

    def __str__(self):
        return (f'{self.__item_no}\t색상:{self.__color}\t{self.__thickness}\t'
                f'{self.__width}x{self.__height}cm\t수량:{self.__qty}\t{self.__amount}원')
