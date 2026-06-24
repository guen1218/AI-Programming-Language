#======================
# 데이터 모델 정의 : Order
class Order:
    STATUS_ORDERED = '주문접수'
    STATUS_SHIPPING = '배송중'
    STATUS_DONE = '배송완료'
    STATUS_CANCELLED = '주문취소'

    def __init__(self, member_no, items, total_price, address, order_date):
        self.__order_no = 0
        self.__member_no = member_no
        self.__items = items          # list of CartItem
        self.__total_price = total_price
        self.__address = address      # 배송지
        self.__order_date = order_date
        self.__status = Order.STATUS_ORDERED

    def get_order_no(self):
        return self.__order_no
    def get_member_no(self):
        return self.__member_no
    def get_items(self):
        return self.__items
    def get_total_price(self):
        return self.__total_price
    def get_address(self):
        return self.__address
    def get_order_date(self):
        return self.__order_date
    def get_status(self):
        return self.__status

    def set_order_no(self, order_no):
        self.__order_no = order_no

    def change_status(self, status):
        self.__status = status

    def __str__(self):
        return (f'[주문 {self.__order_no}] {self.__order_date}\t'
                f'회원번호:{self.__member_no}\t금액:{self.__total_price}원\t'
                f'배송지:{self.__address}\t상태:{self.__status}')
