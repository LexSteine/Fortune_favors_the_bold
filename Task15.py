def TankRush(H1, W1, S1, H2, W2, S2):
    result = []
    S1 = S1.split()
    S2 = S2.split()
    result = FindFirstChar(H1, W1, S1, H2, W2, S2)
    return result


def FindFirstChar(H1, W1, S1, H2, W2, S2):
    result = False
    for i in range(H1):
        for j in range(W1):
            if S1[i][j] == S2[0][0] and (i + H2 <= H1) and (j + W2 <= W1):
                result = FindOtherChars(H1, W1, S1, H2, W2, S2, i, j)
            if result:
                break
        if result:
            break
    return result


def FindOtherChars(H1, W1, S1, H2, W2, S2, H1first, W1first):
    result = True
    for i in range(H2):
        for j in range(W2):
            if S1[H1first + i][W1first + j] != S2[i][j]:
                result = False
                break
        if not result:
            break
    return result
