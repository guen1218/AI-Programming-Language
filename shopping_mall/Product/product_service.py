from Product.product_dao import ProductDAO
from Product.product import Product
#==================
# 상품(아크릴 판 단가/재고) 서비스 로직 : ProductService
class ProductService:
    def __init__(self, productDao):
        self.__dao = productDao

    # 초기 설정 등록 (기본단가, 재고)
    def init_product(self, base_price, stock=0):
        return self.__dao.set_product(Product(base_price, stock))

    def get_product(self):
        return self.__dao.get_product()

    def get_base_price(self):
        return self.__dao.get_product().get_base_price()

    def get_stock(self):
        return self.__dao.get_product().get_stock()

    def set_base_price(self, base_price):
        product = self.__dao.get_product()
        if not product:
            return False
        product.set_base_price(base_price)
        return True

    def set_stock(self, stock):
        product = self.__dao.get_product()
        if not product:
            return False
        product.set_stock(stock)
        return True

    # 주문 완료 시 재고 감소
    def decrease_stock(self, qty):
        return self.__dao.get_product().decrease_stock(qty)

    # 주문 취소 시 재고 복구
    def increase_stock(self, qty):
        self.__dao.get_product().increase_stock(qty)
        return True


# 단위 테스트
if __name__ == '__main__':
    psv = ProductService(ProductDAO())
    psv.init_product(5, 100)
    print(psv.get_product())
    print('견적:', Product.calc_price(psv.get_base_price(), 10, 20, '5T', 2))
    psv.decrease_stock(3)
    print('재고:', psv.get_stock())
