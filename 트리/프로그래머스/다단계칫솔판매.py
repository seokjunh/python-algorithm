def solution(enroll:list, referral:list, seller:list, amount:list) -> list:
    money = [0] * len(enroll)
    d = {}
    for i, e in enumerate(enroll):
        d[e] = i
    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = d[s]
            money[idx] += m - m // 10
            m //= 10
            s = referral[idx]
    return money

print(solution(enroll=["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], referral=["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], seller=["young", "john", "tod", "emily", "mary"], amount=[12, 4, 2, 5, 10]))