from Book.book_dao import BookDAO
from Book.book import Book
#==================
# 도서 관리 서비스 로직 : BookService (BOOK-001 ~ BOOK-006)
class BookService:
    def __init__(self, bookDao):
        self.__dao = bookDao
    def add_book(self, title, author, publisher, price, stock=0):
        book = Book(title, author, publisher, price, stock)
        return self.__dao.insert_book(book)
    def show_books(self):
        return self.__dao.get_all_books()

    # 도서 상세 조회
    def detail_book(self, book_no):
        return self.__dao.get_book(book_no)
    def edit_book(self, book_no, title, author, publisher, price):
        book = self.__dao.get_book(book_no)
        if not book:
            return False
        book.update_info(title, author, publisher, price)
        return self.__dao.update_book(book_no, book)
    def delete_book(self, book_no):
        return self.__dao.remove_book(book_no)
    def decrease_stock(self, book_no, qty):
        book = self.__dao.get_book(book_no)
        if not book:
            return False
        result = book.decrease_stock(qty)
        if result:
            self.__dao.update_book(book_no, book)
        return result

    # 재고 증가 (주문 취소 시 호출)
    def increase_stock(self, book_no, qty):
        book = self.__dao.get_book(book_no)
        if not book:
            return False
        book.increase_stock(qty)
        self.__dao.update_book(book_no, book)
        return True
    def update_stock(self, book_no, stock):
        book = self.__dao.get_book(book_no)
        if not book:
            return False
        book.set_stock(stock)
        return self.__dao.update_book(book_no, book)

    def search_book(self, keyword):
        pass
