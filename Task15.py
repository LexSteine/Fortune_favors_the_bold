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

# def SearchInRow(H1, W1, S1, H2, W2, S2):
#     result = []
#     for row in S1:
#         result = SearchInColumn(row, H1, W1, S1, H2, W2, S2)
#     return result
#
#
# def SearchInColumn(row, H1, W1, S1, H2, W2, S2):
#     result = []
#     for column in row:
#         result = FindInRow(column, H1, W1, S1, H2, W2, S2)
#     return result
#
#
# def FindInRow(column, H1, W1, S1, H2, W2, S2):
#     result = []
#     for row2 in S2:
#         result = FindInColumn(column, row2, H1, W1, S1, H2, W2, S2)
#     return result
#
#
# def FindInColumn(column, row2, H1, W1, S1, H2, W2, S2):
#     result = []
#     for column2 in row2:
#         if column2 == column:
#             result = Check(column, row2, H1, W1, S1, H2, W2, S2)
#     return result
#
#
# def Check(column, row2, H1, W1, S1, H2, W2, S2):
#     result = []
#     # for i in range(len(H1)):
#     #     result.append()
#     return result

# если найден первый элемент S2 в S1, то:
# по каждому элементу S2 нужно проверить соответствие элемента S1
# в таком же месте относительно первого найденного элемента
