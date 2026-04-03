def recursion(a, l, r, con):
    con+=1
    if l >= r: return 1,con
    elif a[l] != a[r]:return "0",con
    else: return recursion(a, l+1, r-1, con)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)

ii = int(input())
for i in range(ii):
    data=[]
    asd = list(input())
    data = isPalindrome(asd)

    print(f'{data[0]} {data[1]}')