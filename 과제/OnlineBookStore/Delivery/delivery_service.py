from Delivery.delivery_dao import DeliveryDAO
from Order.order import Order
#==================
# 배송 관리 서비스 로직 : DeliveryService (DELI-001 ~ DELI-003)
class DeliveryService:
    def __init__(self, deliveryDao, orderService, memberService):
        self.__dao = deliveryDao
        self.__order_service = orderService
        self.__member_service = memberService

    def __get_member_address(self, member_no):
        member = self.__member_service.view_member_info_by_no(member_no)
        if member:
            return member.get_address()
        return '주소 없음'
    def view_my_delivery(self, member_no):
        orders = self.__order_service.view_my_orders(member_no)
        result = []
        for order in orders:
            address = self.__get_member_address(member_no)
            from Delivery.delivery import Delivery
            result.append(Delivery(order.get_order_no(), member_no, address, order.get_order_status()))
        return result
    def view_all_deliveries(self):
        orders = self.__order_service.view_all_orders()
        result = []
        for order in orders:
            address = self.__get_member_address(order.get_member_no())
            from Delivery.delivery import Delivery
            result.append(Delivery(order.get_order_no(), order.get_member_no(), address, order.get_order_status()))
        return result
    def update_delivery_status(self, order_no, status):
        return self.__order_service.update_delivery_status(order_no, status)
