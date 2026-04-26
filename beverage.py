menu = {"아메리카노":5000, "아이스아메리카노":5500, "라떼":6000, "녹차":5500, "허니브레드":8000}
naeyok = []
def see_menu():
    print("=======================================================================================================================")
    for key, val in menu.items():
        print(f"{key} : {val}원", end="\t")
    print("\n=======================================================================================================================\n")

def jumun(sum):
    key, su = input("메뉴 이름과 개수를 입력하시오(예시: 아메리카노 3) : ").split()
    for i in range(int(su)):
        naeyok.append(key)
    sum += menu[key] * int(su)
    a = input("다른 주문 메뉴 있으신가요? 예 아니오 : ")
    if  a == "예" :
        print("추가 주문을 진행합니다 \n")
        return jumun(sum)
    elif a == "아니오":
        print("주문을 종료합니다 \n")
        return sum
    else :
        print("그냥 주문 더 하세요")
        return jumun(sum)
    
def don(donn):
    money = int(input("얼마를 내실건가요? : "))
    if donn > money :
        return False
    else :
        return money - donn
    
def youngsuzng():
    for j in set(naeyok):
        suii = naeyok.count(j)
        print(f"{j}: {suii}개 {menu[j]*suii}원")

see_menu()
ju = jumun(0)
print(f"{ju}원입니다 고객님")

dddon = don(ju)
if dddon:
    print(f"잔액은 {dddon}원 입니다\n")
    youngsuzng()
else :
    print("잔액이 부족합니다")

