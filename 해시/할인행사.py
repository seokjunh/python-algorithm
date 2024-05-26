from collections import Counter
def solution(want, number, discount):
    
    wishlist = {}
    for i in range(len(want)):
        wishlist[want[i]] = number[i]
    wishlist = Counter(wishlist)

    answer = 0
    
    i = 0
    while True:
        l = Counter(discount[i:i+10])
        a = wishlist - l
        if not a:
            answer += 1
        if i+10 == len(discount):
            break
        i += 1
    return answer