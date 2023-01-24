def BiggerGreater(input):
    s = []
    s += [i for i in input]
    answer = two(s)
    return answer if input != answer else ""

def two(m):
    f = False
    for i in range(len(m) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if m[i] > m[j]:
                m[i], m[j] = m[j], m[i]
                f = True
                m[j:] = three(m[j:])
                break
        if f:
            break
    r = ""
    for i in range(len(m)):
        r += m[i]
    return r


def three(m):
    for i in range(1, len(m) - 1):
        for j in range(i + 1, len(m)):
            if m[i] > m[j]:
                m[i],m[j] = m[j],m[i]
    return m
