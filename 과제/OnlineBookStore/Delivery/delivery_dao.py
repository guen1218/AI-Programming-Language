from Delivery.delivery import Delivery
#====================
# 배송 데이터 접근 : DeliveryDAO
# 배송 상태는 orderDB의 order_status로 관리 (DATA-005)
# DeliveryDAO는 Delivery 뷰 객체를 조회 전용으로 생성
class DeliveryDAO:
    def __init__(self, orderDao):
        self.__orderDao = orderDao   # OrderDAO 참조

    def get_delivery(self, order_no, address):
        order = self.__orderDao.get_order(order_no)
        if not order:
            return None
        return Delivery(order.get_order_no(), order.get_member_no(), address, order.get_order_status())

    def get_all_deliveries(self, member_address_map):
        orders = self.__orderDao.get_all_orders()
        result = []
        for order in orders:
            address = member_address_map.get(order.get_member_no(), '주소 없음')
            result.append(Delivery(order.get_order_no(), order.get_member_no(), address, order.get_order_status()))
        return result
