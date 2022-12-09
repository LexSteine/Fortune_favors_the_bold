def PatternUnlock(N, hits):
    Points = {1: [1, 2], 2: [2, 2], 3: [3, 2], 4: [3, 1], 5: [2, 1], 6: [1, 1], 7: [3, 3], 8: [2, 3], 9: [1, 3]}
    for i in range(0, len(hits) - 1):
        if checkOnDiagonal(Points, hits[i], hits[i + 1]):
            N += 0.414213562
    N = toFixed(N - 1, 5).split(".")
    result = ""
    for j in N[0]:
        if j != "0":
            result += j
    for i in N[1]:
        if i != "0":
            result += i
    return result


def checkOnDiagonal(Points, current, next):
    if 1 < (abs(Points.get(current)[0] - Points.get(next)[0]) +
            abs(Points.get(current)[1] - Points.get(next)[1])):
        return True
    return False


def toFixed(number, digits=0):
    return f"{number:.{digits}f}"
