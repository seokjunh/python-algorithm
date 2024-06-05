while True:
    try:
        def cantor(n):
            if n == 0:
                return "-"
            return cantor(n-1) + " "* (3**(n-1)) + cantor(n-1)
        
        N = int(input())
        print(cantor(N))
    except EOFError:
        break