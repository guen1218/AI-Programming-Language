# 1. 자료구조 
board_screen = ' 0 | 1 | 2 \n 3 | 4 | 5 \n 6 | 7 | 8\n'  #화면에 보여줄 보드
board = [" "] * 9 # 게임의 진행 상태
win_status = [(0,1,2), (3,4,5), (6,7,8),  # 이겼을 때의 상태
              (0,3,6), (1,4,7), (2,5,8),
              (0,4,8), (2,4,6)]


human = 'O'
computer = 'X'
# 2. 필요한 함수 정의
def showbord():
    print(board_screen)

def updateGame(who, number):
    global board_screen, board
    if board[number] != " ":
        print("다시하세욧")
        return 0
    board[number] = who
    board_screen = board_screen.replace(str(number), who)

def GetComputerNumber():
    for i in range (len(board)):
        if board[i] == " ":
            return i
    return -1

def isWin(turn):
    for status in win_status:
        if board[status[0]] == board[status[1]] == board[status[2]] == turn:
            return True
    return False
# 3. 메인 로직
# 3-1. 필요한 자료구조 초기화

print('========== Tic-Tac-Toe ==========')
# 3-2. 보드를 보여줌
showbord()
while True:
    # 3-3. human 차례
    # human 입력 받아서 처리
    human_input = int(input('숫자를 입력하세요 : '))
    if updateGame(human, human_input) == 0: 
        continue
    showbord()

    if isWin(human): 
        print("YOU WIN~~~~~~~~~~~~~~~~~~!!!")
        break #human win

    

    # 3-4. computer 차례
    # computer가 놓을 자리를 선택
    computer_input = GetComputerNumber()
    updateGame(computer, computer_input)
    showbord()
    if isWin(computer) : 
        print("YOU LOOOOOOOOSSSSSSSSSSSSSSSSSSSE~~~~")
        break # CPU win
    if computer_input == -1:
        print("the gamed ended in a tie ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~!~!~!~")
        #비겼음
        break