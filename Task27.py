def Football(F, N):
    if N == 2 and F[1] < F[0]:
        return True
    elif N == 1 or (N == 2 and F[1] >= F[0]):
        return False
    AscOrder = True
    bigIndex, smallIndex = -1, -1
    for i in range(1, N):
        if F[i - 1] > F[i]:
            AscOrder = False
            bigIndex = i - 1
            break
    if not AscOrder:
        smallIndex = SearchLastMin(F, bigIndex)
        Mcheck = FirstAlgo(F, bigIndex, smallIndex)
        AscOrder = CheckAscOrder(Mcheck)
    else:
        return False
    if not AscOrder:
        Mcheck = SecondAlgo(F, bigIndex, smallIndex)
        AscOrder = CheckAscOrder(Mcheck)
    return AscOrder


def SearchLastMin(InputMassiv, startIndex):
    lastIndex = -1
    M = [InputMassiv[i] for i in range(len(InputMassiv))]
    for i in range(startIndex + 1, len(M)):
        if M[i] < M[startIndex]:
            lastIndex = i
    return lastIndex


def FirstAlgo(InputMassiv, startIndex, endIndex):
    M = [InputMassiv[i] for i in range(len(InputMassiv))]
    if endIndex != -1:
        M[startIndex], M[endIndex] = M[endIndex], M[startIndex]
    else:
        M[startIndex], M[startIndex - 1] = M[startIndex - 1], M[startIndex]
    return M


def SecondAlgo(InputMassiv, startIndex, endIndex):
    M = [InputMassiv[i] for i in range(len(InputMassiv))]
    for i in range(endIndex - startIndex + 1):
        M[startIndex + i] = M[endIndex - i]
    return M


def CheckAscOrder(M):
    flag = False
    for i in range(1, len(M)):
        if M[i - 1] <= M[i]:
            flag = True
        else:
            flag = False
            break
    return flag
