class MemberService:
    def __init__(self):
        self.mem_list = []

    def create_mem(self, num, id, pas, name, pon, add):
        self.mem_list.append(Member(num, id, pas, name, pon, add))
class Member:
    def __init__(self, num, id, pas, name, pon, add):
        self.num = num
        self.id = id
        self.pas = pas
        self.name = name
        self.pon = pon
        self.add = add
    
    def __str__(self):
        return (f"[회원정보] 번호: {self.num} | 아이디: {self.id} | "
                f"이름: {self.name} | 연락처: {self.pon} | 주소: {self.add}")