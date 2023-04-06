def Keymaker(k):
    D, Doors = [0 for i in range(k)], ""
    for i in range(k):
        for j in range(i, k, i + 1):
            D[j] = ChangeState(D[j])
    for i in range(len(D)):
        Doors += str(D[i])
    return Doors


def ChangeState(elem):
    if elem == 1:
        return 0
    else:
        return 1
