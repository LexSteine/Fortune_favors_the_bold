def squirrel(N):
    factorial = 1
    while N > 0:
        factorial = factorial * N
        N -= 1
    while factorial > 10:
        factorial //= 10
    return factorial
