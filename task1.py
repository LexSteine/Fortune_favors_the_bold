def squirrel(N):
    if N == 0:
        factorial = N
    else:
        factorial = 1
        while N > 0:
            factorial = factorial * N
            N -= 1
        while factorial > 10:
            factorial //= 10
    return factorial