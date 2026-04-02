from collections import deque
queue = deque()

print ('''
================================================
 1. enqueue  2. Dequeue  3. Get Front   0. Exit
================================================
''')

def enqueue(data):
    queue.append(data)
    
def dequeue():
    if queue :
        data = queue.popleft()
    else :
        data = -1
    return data

def getFront():
    if queue : return queue[0]
    return -1
        
print('시작')

while True :
    data = 0
    #메뉴 프린트
    #메뉴 번호 입력
    menu = int(input(">> 연산 메뉴 선택 : "))

    if menu == 0 : break
    
    if menu == 1 : #enqueue
        data = int(input(">> 추가할 데이터 입력 : "))
        enqueue(data)
        
    elif menu == 2: #dequeue
        data = dequeue()
        if data != -1 :
            print("가져온 데이터 : ",data, end =" ")
        else :
            print("Queue가 비어있습니다.", end =" ")

    elif menu == 3: #peek
        data = getFront()
        if data != -1 :
            print("가져온 데이터 : ",data, end =" ")
        else :
            print("Queue가 비어있습니다.", end =" ")

    else :
        print("다시하세욧")
        
    print ("[Queue]",end=' ')    
    for i in queue :
        print(f"{i} ",end='')
    print()
print("종료")
