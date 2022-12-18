def TheRabbitsFoot(s, encode):  # str, bool. return str
    result = ""
    if encode:
        result = DoShifr(s)
    else:
        result = DoDeshifr(s)
    return result


def DoShifr(s):
    s = "".join(s.split())
    length = len(s) ** 0.5
    matrix = []
    result = ""
    if length.is_integer():
        N, M = int(length), int(length)
    else:
        N, M = int(length // 1), int((length // 1) + 1)
    if N * M < len(s):
        N += int((len(s) - N * M) // 1)
    for i in range(N):
        matrix.append("")
        while s != "" and len(matrix[i]) < M:
            matrix[i] += s[:1]
            s = s[1:]
    for i in range(M):
        for j in matrix:
            result += j[0]
            matrix[matrix.index(j)] = j[1:]
            if matrix[len(matrix) - 1] == "":
                matrix.remove("")
        result += " "
    return result[:len(result) - 1]


def DoDeshifr(s):
    N = len(s.split()[0])
    M = len(s.split())
    s = s.split()
    result = ""
    for i in s:
        if len(i) < N:
            for j in range(len(i), N):
                s[s.index(i)] += " "
    for i in range(N):
        for j in range(M):
            result += s[j][i]
    return result.rstrip()
