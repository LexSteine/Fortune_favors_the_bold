def ConquestCampaign(N, M, L, battalion):
    D, C = 1, []
    def check(x, y, li):
        i = 0
        while i < len(li):
            if (x == li[i]) and (y == li[i + 1]):
                return False
            i += 2
        return True
    def landing(x, y, l):
        l.append(x)
        l.append(y)
        return l
    #cl = lambda x, y, l: if check(x, y, l): landing(x, y, l)
    while L != 0:
        #lambda x, y, l: if check(x, y, l): landing(x, y, l)
        if check(battalion[L * 2 - 2], battalion[L * 2 - 1],C): landing(battalion[L * 2 - 2], battalion[L * 2 - 1],C)
        L -= 1
    while len(C) != N * M * 2:
        L = len(C) - 2
        while L >= 0:
            if (C[L] > 1):
                if check(C[L] - 1, C[L + 1], C): landing(C[L] - 1, C[L + 1], C)
            if (C[L] < N):
                if check(C[L] + 1, C[L + 1], C): landing(C[L] + 1, C[L + 1], C)
            if (C[L + 1] > 1):
                if check(C[L], C[L + 1] - 1, C): landing(C[L], C[L + 1] - 1, C)
            if (C[L + 1] < M):
                if check(C[L], C[L + 1] + 1, C): landing(C[L], C[L + 1] + 1, C)
            L -= 2
        D += 1
    return D