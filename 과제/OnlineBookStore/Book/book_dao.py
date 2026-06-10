from Book.book import Book
#====================
# 도서 데이터 접근 (CRUD) : BookDAO
class BookDAO:
    def __init__(self):
        self.__bookDB = {}   # Key: book_no, Value: Book
        self.__next_no = 1

    def insert_book(self, book):
        book.set_book_no(self.__next_no)
        self.__bookDB[self.__next_no] = book
        self.__next_no += 1
        return True

    def is_exist(self, book_no):
        return book_no in self.__bookDB

    def get_book(self, book_no):
        return self.__bookDB.get(book_no, None)

    def get_all_books(self):
        return list(self.__bookDB.values())

    def update_book(self, book_no, book):
        if self.is_exist(book_no):
            self.__bookDB[book_no] = book
            return True
        return False

    def remove_book(self, book_no):
        if self.is_exist(book_no):
            self.__bookDB.pop(book_no)
            return True
        return False
