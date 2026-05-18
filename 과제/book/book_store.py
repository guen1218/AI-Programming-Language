import book

madang = Bookstore()
madang.add_book(Book(1, "책", "출판사", 10000))
madang.add_book(Book(2, "책디스아웃", "정상수", 13000))
madang.add_book(Book(3, "개발자를 위한 필수 수학", "한빛미디어", 27000))
madang.add_book(Book(4, "오라클로 배우는 데이터베이스 개론과 실습", "한빛아카데미", 30000))

madang.purchase()
