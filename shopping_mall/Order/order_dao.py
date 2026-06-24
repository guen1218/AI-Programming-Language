from Order.order import Order
#====================
# 주문 데이터 접근 (CRUD) : OrderDAO
class OrderDAO:
    def __init__(self):
        self.__orderDB = {}   # Key: order_no, Value: Order
        self.__next_no = 1

    def insert_order(self, order):
        order.set_order_no(self.__next_no)
        self.__orderDB[self.__next_no] = order
        self.__next_no += 1
        return order

    def get_order(self, order_no):
        return self.__orderDB.get(order_no, None)

    def get_all_orders(self):
        return list(self.__orderDB.values())

    # 특정 회원의 주문 목록
    def get_orders_by_member(self, member_no):
        return [o for o in self.__orderDB.values() if o.get_member_no() == member_no]

    def update_order(self, order_no, order):
        if order_no in self.__orderDB:
            self.__orderDB[order_no] = order
            return True
        return False
