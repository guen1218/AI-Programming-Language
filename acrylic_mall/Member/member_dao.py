from Member.member import Member
#====================
# 회원 데이터 접근 (CRUD) : MemberDAO
class MemberDAO:
    def __init__(self):
        self.__memberDB = {}   # Key: id, Value: Member
        self.__next_no = 1

    def insert_member(self, member):
        if self.is_exist(member.get_id()):
            return False
        member.set_member_no(self.__next_no)
        self.__memberDB[member.get_id()] = member
        self.__next_no += 1
        return True

    def is_exist(self, id):
        return id in self.__memberDB

    def get_member_info(self, id):
        return self.__memberDB.get(id, None)

    def get_all_members(self):
        return list(self.__memberDB.values())

    def update_member_info(self, id, member):
        if self.is_exist(id):
            self.__memberDB[id] = member
            return True
        return False

    def remove_member(self, id):
        if self.is_exist(id):
            self.__memberDB.pop(id)
            return True
        return False


# 단위 테스트
if __name__ == '__main__':
    dao = MemberDAO()
    dao.insert_member(Member('user1', '1234', '이근휘', '01012345678', 'a@a.com', '서울'))
    print(dao.get_member_info('user1'))
