#======================
# 데이터 모델 정의 : Product (아크릴 판 단일 설정)
#  - 카탈로그(상품 목록) 없이 하나의 기본단가와 재고만 관리한다.
#  - 색상/두께/규격은 견적 단계에서 선택하는 옵션이다.
class Product:
    # 견적 시 선택 가능한 색상 (특정 색상만 허용)
    COLORS = ['투명', '검정', '흰색', '빨강', '파랑', '노랑']

    # 두께 옵션과 가격 배율
    THICKNESS_RATIO = {'2T': 1.0, '3T': 1.2, '5T': 1.5, '8T': 2.0}

    def __init__(self, base_price, stock=0):
        self.__base_price = base_price   # cm² 당 기본단가
        self.__stock = stock             # 재고 (장)

    def get_base_price(self):
        return self.__base_price
    def get_stock(self):
        return self.__stock

    def set_base_price(self, base_price):
        self.__base_price = base_price
    def set_stock(self, stock):
        self.__stock = stock

    def decrease_stock(self, qty):
        if self.__stock < qty:
            return False
        self.__stock -= qty
        return True

    def increase_stock(self, qty):
        self.__stock += qty

    # 견적 계산 : 기본단가 × 가로 × 세로 × 두께배율 × 수량
    @staticmethod
    def calc_price(base_price, width, height, thickness, qty):
        ratio = Product.THICKNESS_RATIO.get(thickness, 1.0)
        return int(base_price * width * height * ratio * qty)

    def __str__(self):
        return f'아크릴 판\t기본단가:{self.__base_price}원/cm²\t재고:{self.__stock}장'
