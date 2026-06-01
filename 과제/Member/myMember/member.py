class MemberService:
    def __init__(self):
        self.mem_list = []

    def create_mem(self, num, id, pas, name, pon, add):
        for m in self.mem_list:
            if m.num == num or m.id == id:
                return False
        self.mem_list.append(Member(num, id, pas, name, pon, add))
        return True

    def see_mem(self):
        for i in self.mem_list:
            print(i.num ,i.name)

    def super_see_mem(self, name):
        for i in self.mem_list:
            if i.name == name:
                return i
        return False
    
    def update_mem(self, name, update, update_data):
        updateList = ["id", "name", "pon", 'add']
        for i in self.mem_list:
            if i.name == name:
                if update in updateList:
                    setattr(i, update, update_data)
                    return True
        return False
    
    def delete_mem(self, name):
        for i in self.mem_list:
            if i.name == name:
                self.mem_list.remove(i)
                return True
        return False
    
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