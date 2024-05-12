try:
    N = int(input())
    s = list(map(int, input().split()))
    v = int(input())
    print(s.count(v))
except EOFError:
    print("더 이상 입력이 없습니다.")