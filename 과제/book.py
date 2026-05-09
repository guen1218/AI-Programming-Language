class Book:
    def __init__(self, bookid, bookname, publisher, price):
        self.bookid = bookid
        self.bookname = bookname
        self.publisher = publisher
        self.price = price

    def get_sale_price(self, discount_rate):
        """할인율을 적용한 실제 판매가를 계산합니다."""
        return int(self.price * (1 - discount_rate))

    def __str__(self):
        return f"[{self.bookid}] {self.bookname:15} | {self.publisher:10} | 정가: {self.price:>6}원"


class Bookstore:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_menu(self):
        print("="*50)
        for book in self.books:
            print(book)
        print("="*50)

    def purchase(self):
        allprice=[]
        while True:
            self.show_menu()
            choice = input("\n구매하실 도서를 입력하세요: ")
            selected_book = next((b for b in self.books if b.bookname == choice), None)

            if not selected_book:
                print("\n해당 도서가 없습니다.")
            else:
                discount = 0.1
                final_price = selected_book.get_sale_price(discount)
                allprice.append(final_price)

                print(f"\n선택하신 도서: {selected_book.bookname}")
                print(f"정가: {selected_book.price}원")
                print(f"할인 적용(10%): {final_price}원")
                
                if input("추가주문 하시겠습니까? 네 아니오 ").strip() == "네":
                    print("그래용")

                else:
                    print(sum(allprice),"원 결제가 완료되었습니다.")
                    break

madang = Bookstore()
madang.add_book(Book(1, "책", "출판사", 10000))
madang.add_book(Book(2, "책디스아웃", "정상수", 13000))
madang.add_book(Book(3, "개발자를 위한 필수 수학", "한빛미디어", 27000))
madang.add_book(Book(4, "오라클로 배우는 데이터베이스 개론과 실습", "한빛아카데미", 30000))

madang.purchase()