def MadMax(N, Tele):
    if N > 1:
        i, j = 0, 1
        while i < N:
            while j < N:
                if Tele[i] > Tele[j]:
                    Tele[i],Tele[j] = Tele[j],Tele[i]
                j += 1
            i += 1
            j = i + 1
        c = 0
        while c < N//2:
            if N//2+c < N-1-c:
                Tele[N//2+c],Tele[N-1-c] = Tele[N-1-c],Tele[N//2+c]
            c += 1
    return Tele
