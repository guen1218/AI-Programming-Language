#======================
# 데이터 모델 정의 : Cart
class Cart:
    def __init__(self, member_no):
        self.__member_no = member_no
        self.__items = {}   # Key: book_no, Value: quantity

    def get_member_no(self):
        return self.__member_no
    def get_items(self):
        return self.__items
    def add_book(self, book_no, qty):
        if book_no in self.__items:
            self.__items[book_no] += qty
        else:
            self.__items[book_no] = qty

    # 수량 변경
    def change_quantity(self, book_no, qty):
        if book_no not in self.__items:
            return False
        self.__items[book_no] = qty
        return True
    def remove_book(self, book_no):
        if book_no in self.__items:
            del self.__items[book_no]
            return True
        return False

    # 장바구니 전체 비우기
    def clear_cart(self):
        self.__items.clear()

    def is_empty(self):
        return len(self.__items) == 0

    def __str__(self):
        return f'회원번호:{self.__member_no}\t담긴도서수:{len(self.__items)}'
