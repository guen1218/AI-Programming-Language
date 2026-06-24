#======================
# 데이터 모델 정의 : Cart
class Cart:
    def __init__(self, member_no):
        self.__member_no = member_no
        self.__items = []        # list of CartItem
        self.__next_item_no = 1

    def get_member_no(self):
        return self.__member_no
    def get_items(self):
        return self.__items

    def add_item(self, item):
        item.set_item_no(self.__next_item_no)
        self.__items.append(item)
        self.__next_item_no += 1

    def get_item(self, item_no):
        for item in self.__items:
            if item.get_item_no() == item_no:
                return item
        return None

    def remove_item(self, item_no):
        item = self.get_item(item_no)
        if item:
            self.__items.remove(item)
            return True
        return False

    def clear(self):
        self.__items.clear()

    def is_empty(self):
        return len(self.__items) == 0

    def total(self):
        return sum(item.get_amount() for item in self.__items)

    def __str__(self):
        return f'회원번호:{self.__member_no}\t담긴항목수:{len(self.__items)}\t총액:{self.total()}원'
