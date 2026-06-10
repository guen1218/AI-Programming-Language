#======================
# 데이터 모델 정의 : Member
class Member:
    def __init__(self, id, password, name, phone='', address=''):
        self.__member_no = 0
        self.__id = id
        self.__password = password
        self.__name = name
        self.__phone = phone
        self.__address = address

    def get_member_no(self):
        return self.__member_no
    def get_id(self):
        return self.__id
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def get_phone(self):
        return self.__phone
    def get_address(self):
        return self.__address

    def set_member_no(self, member_no):
        self.__member_no = member_no
    def set_id(self, id):
        self.__id = id
    def set_password(self, password):
        self.__password = password

    def set_name(self, name):
        self.__name = name
    def update_info(self, name, phone, address):
        self.__name = name
        self.__phone = phone
        self.__address = address

    def check_password(self, password):
        return self.__password == password

    def __str__(self):
        return f'{self.__member_no}\t{self.__id}\t{self.__name}\t전화:{self.__phone}\t주소:{self.__address}'