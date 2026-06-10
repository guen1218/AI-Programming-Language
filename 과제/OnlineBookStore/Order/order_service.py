from Order.order_dao import OrderDAO
from Order.order import Order
#==================
# 주문/배송 관리 서비스 로직 : OrderService (ORDER-001 ~ ORDER-004)
class OrderService:
    def __init__(self, orderDao):
        self.__dao = orderDao
    def create_order(self, member_no, order_items, total_price):
        order = Order(member_no, order_items, total_price)
        self.__dao.insert_order(order)
        return order
    def view_my_orders(self, member_no):
        return self.__dao.get_orders_by_member(member_no)
    def cancel_order(self, order_no, member_no):
        order = self.__dao.get_order(order_no)
        if not order:
            return False
        if order.get_member_no() != member_no:
            return False
        if order.get_order_status() != Order.STATUS_ORDERED:
            return False
        order.change_status(Order.STATUS_CANCELLED)
        return self.__dao.update_order(order_no, order)
    def view_all_orders(self):
        return self.__dao.get_all_orders()
    def reject_order(self, order_no):
        order = self.__dao.get_order(order_no)
        if not order:
            return False
        order.change_status(Order.STATUS_REJECTED)
        return self.__dao.update_order(order_no, order)

    # 배송 상태 변경 (관리자 - DELI-003 연계)
    def update_delivery_status(self, order_no, status):
        order = self.__dao.get_order(order_no)
        if not order:
            return False
        order.change_status(status)
        return self.__dao.update_order(order_no, order)

    def get_order(self, order_no):
        return self.__dao.get_order(order_no)
