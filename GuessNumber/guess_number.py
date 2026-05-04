# 1. 컴퓨터가 숫자를 생각한다 (1 ~ 50)
# 2. 사용자 숫자를 말한다
# 3. 숫자가 맞으면 사용자 win
# 4. 틀리면 컴퓨터가 up, down을 알려준다.
# 5. 2 ~ 4번까지 7번 반복
# 6. 7번 내에 맞추지 못하면 computer win
import random
# limit_num = int(input("어디까지의 수까지 하시겠습니까"))
# trys = bit_length()
limit_num = 50
trys = 7
count = 0
computer_number = random.randint(1, limit_num)

for _ in range(trys):
    user_num=int(input("숫자를 입력하시오:"))
    if user_num == computer_number :
        print("잘하는!")
        break
    print("높은!" if user_num > computer_number else "낮은!")
else:
    print("못하는! 정답: ",computer_number)
