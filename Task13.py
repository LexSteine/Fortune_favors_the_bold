def UFO(N, data, octal):
    if octal:
        result = From8(N, data)
    else:
        result = From16(N, data)
    return result


def From8(N, data):
    result = [0] * N
    i = 0
    for i in range(N):
        for j in range(len(str(data[i]))):
            result[i] += 8 ** (len(str(data[i])) - 1 - j) * int(str(data[i])[j])
    return result


def From16(N, data):
    result = [0] * N
    i = 0
    for i in range(N):
        for j in range(len(str(data[i]))):
            result[i] += 16 ** (len(str(data[i])) - 1 - j) * int(str(data[i])[j])
    return result
