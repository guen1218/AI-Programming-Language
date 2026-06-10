#======================
# 데이터 모델 정의 : Delivery (주문의 배송 정보 뷰)
class Delivery:
    def __init__(self, order_no, member_no, address, status):
        self.__order_no = order_no
        self.__member_no = member_no
        self.__address = address      # 배송지 주소
        self.__status = status        # 주문접수 / 배송중 / 배송완료

    def get_order_no(self):
        return self.__order_no
    def get_member_no(self):
        return self.__member_no
    def get_address(self):
        return self.__address
    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f'주문번호:{self.__order_no}\t회원번호:{self.__member_no}\t배송지:{self.__address}\t상태:{self.__status}'
