from collections import deque
queue = deque()

N = int(input())
for _ in range(N) :
    op_list = input().split()

    if op_list[0] == "push" :
        queue.append(int(op_list[1]))
    elif op_list[0] == 'pop' :
        print(queue.popleft() if queue else -1)
    elif op_list[0] == 'size':
        print(len(queue))
    elif op_list[0] == 'empty' :
        print(0 if queue else 1)
    elif op_list[0] == 'front':
        print(queue[0] if queue else -1)
    elif op_list[0] == 'back':
        print(queue[-1] if queue else -1)