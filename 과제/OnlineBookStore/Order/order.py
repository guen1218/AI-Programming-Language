#======================
# 데이터 모델 정의 : Order
class Order:
    STATUS_ORDERED = '주문접수'
    STATUS_SHIPPING = '배송중'
    STATUS_DONE = '배송완료'
    STATUS_CANCELLED = '주문취소'
    STATUS_REJECTED = '주문거부'

    def __init__(self, member_no, order_items, total_price):
        self.__order_no = 0
        self.__member_no = member_no
        self.__order_items = order_items  # dict: {book_no: qty}
        self.__total_price = total_price
        self.__order_status = Order.STATUS_ORDERED

    def get_order_no(self):
        return self.__order_no
    def get_member_no(self):
        return self.__member_no
    def get_order_items(self):
        return self.__order_items
    def get_total_price(self):
        return self.__total_price
    def get_order_status(self):
        return self.__order_status

    def set_order_no(self, order_no):
        self.__order_no = order_no

    def change_status(self, status):
        self.__order_status = status

    def __str__(self):
        return f'{self.__order_no}\t회원번호:{self.__member_no}\t총액:{self.__total_price}원\t상태:{self.__order_status}'
