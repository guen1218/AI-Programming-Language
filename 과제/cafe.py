class Book:
    def __init__(self, id, name, pub, price):
        self.id = id
        self.name = name
        self.pub = pub
        self.price = price

    def salePrice(self, discount):
        return int(self.price * (1 - discount))

    def addBook(self, id, name, pub, price):
        