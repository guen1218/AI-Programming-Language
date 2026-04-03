from collections import deque
queue = deque()

N, K = map(int, input().split())

#queue에 숫자를 모두 enqueue
for i in range(1, N+1):
    queue.append(i)

count=1
print("<",end='')
while len(queue)>1:
    person = queue.popleft()
    if count != K:
        queue.append(person)
        count+=1
    else:
        print(person, end=", ")
        count=1

print(queue.popleft(),end='>')