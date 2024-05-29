def recursion(t,l,r):
    global cnt
    if l >= r: 
        return 1
    elif t[l] != t[r]:
        return 0
    else: 
        cnt += 1
        return recursion(t, l+1, r-1)

def isPalindrome(T):
    global cnt
    cnt = 1
    return recursion(T, 0, len(T)-1)

for i in range(int(input())):
    T = input()
    print(isPalindrome(T),cnt)