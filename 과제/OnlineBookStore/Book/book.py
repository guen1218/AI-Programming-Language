#======================
# 데이터 모델 정의 : Book
class Book:
    def __init__(self, title, author, publisher, price, stock=0):
        self.__book_no = 0
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = price
        self.__stock = stock

    def get_book_no(self):
        return self.__book_no
    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_publisher(self):
        return self.__publisher
    def get_price(self):
        return self.__price
    def get_stock(self):
        return self.__stock

    def set_book_no(self, book_no):
        self.__book_no = book_no
    def set_title(self, title):
        self.__title = title
    def set_author(self, author):
        self.__author = author
    def set_publisher(self, publisher):
        self.__publisher = publisher
    def set_price(self, price):
        self.__price = price
    def set_stock(self, stock):
        self.__stock = stock

    def update_info(self, title, author, publisher, price):
        self.__title = title
        self.__author = author
        self.__publisher = publisher
        self.__price = price

    def decrease_stock(self, qty):
        if self.__stock < qty:
            return False
        self.__stock -= qty
        return True

    def increase_stock(self, qty):
        self.__stock += qty

    def __str__(self):
        return f'{self.__book_no}\t{self.__title}\t{self.__author}\t{self.__publisher}\t{self.__price}원\t재고:{self.__stock}'
