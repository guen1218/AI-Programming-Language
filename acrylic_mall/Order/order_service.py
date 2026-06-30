from datetime import datetime
from Order.order_dao import OrderDAO
from Order.order import Order
#==================
# 주문 서비스 로직 : OrderService
class OrderService:
    def __init__(self, orderDao):
        self.__dao = orderDao

    def create_order(self, member_no, items, total_price, address):
        order_date = datetime.now().strftime('%Y-%m-%d %H:%M')
        order = Order(member_no, list(items), total_price, address, order_date)
        return self.__dao.insert_order(order)

    def get_order(self, order_no):
        return self.__dao.get_order(order_no)

    def view_my_orders(self, member_no):
        return self.__dao.get_orders_by_member(member_no)

    # 관리자 : 전체 주문 조회
    def view_all_orders(self):
        return self.__dao.get_all_orders()

    # 주문 취소
    def cancel_order(self, order_no, member_no):
        order = self.__dao.get_order(order_no)
        if not order or order.get_member_no() != member_no:
            return False
        if order.get_status() != Order.STATUS_ORDERED:
            return False
        order.change_status(Order.STATUS_CANCELLED)
        return self.__dao.update_order(order_no, order)

    # 관리자 : 배송 상태 변경
    def update_status(self, order_no, status):
        order = self.__dao.get_order(order_no)
        if not order:
            return False
        order.change_status(status)
        return self.__dao.update_order(order_no, order)
