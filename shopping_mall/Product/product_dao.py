from Product.product import Product
#====================
# 상품 데이터 접근 : ProductDAO
#  - 아크릴 판 설정(단가/재고) 하나만 보관한다.
class ProductDAO:
    def __init__(self):
        self.__product = None   # 단일 Product

    def set_product(self, product):
        self.__product = product
        return True

    def get_product(self):
        return self.__product


# 단위 테스트
if __name__ == '__main__':
    dao = ProductDAO()
    dao.set_product(Product(5, 100))
    print(dao.get_product())
