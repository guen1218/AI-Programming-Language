from Member.member_dao import MemberDAO
from Member.member import Member
#==================
# 회원 관리 서비스 로직 : MemberService
class MemberService:
    ADMIN_ID = 'admin'
    ADMIN_PASSWORD = '123'

    def __init__(self, memberDao):
        self.__dao = memberDao
        # 관리자 계정 기본 등록
        self.join(Member(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD, '관리자'))
        self.current_user = None

    def join(self, member):
        return self.__dao.insert_member(member)

    def login(self, id, password):
        member = self.__dao.get_member_info(id)
        if member and member.check_password(password):
            self.current_user = id
            return True
        return False

    def logout(self):
        self.current_user = None

    def is_admin(self):
        return self.current_user == MemberService.ADMIN_ID

    def list_members(self):
        return self.__dao.get_all_members()

    def view_member_info(self, id):
        return self.__dao.get_member_info(id)

    def update_member_info(self, id, phone, email, address):
        member = self.__dao.get_member_info(id)
        if not member:
            return False
        member.update_info(phone, email, address)
        return self.__dao.update_member_info(id, member)

    def remove_member(self, id):
        return self.__dao.remove_member(id)

    # member_no로 회원 조회 (주문/장바구니 연계용)
    def view_member_info_by_no(self, member_no):
        for m in self.__dao.get_all_members():
            if m.get_member_no() == member_no:
                return m
        return None


# 단위 테스트
if __name__ == '__main__':
    msv = MemberService(MemberDAO())
    msv.join(Member('user1', '1234', '이근휘'))
    print(msv.login('user1', '1234'), msv.current_user)
    print(msv.login(MemberService.ADMIN_ID, MemberService.ADMIN_PASSWORD), msv.is_admin())
