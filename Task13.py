def UFO(N, data, octal):
    if octal:
        result = From8(data)
    else:
        result = From16(data)
    return result


def From8(data):
    result = []
    for i in data:
        result.append(0)
        for j in str(i):
            # print(8 ** str(i).index(j))
            print(i % 10 ** (1 + str(i).index(j)))
            print(1 + str(i).index(j))
            print("конец")
            result[data.index(i)] += 8 ** str(i).index(j) * (i % 10 ** (1 + str(i).index(j)))
    return result


def From16(data):
    result = []
    for i in data:
        result.append(0)
        for j in str(i):
            result[data.index(i)] += 16 ** data.index(i) * (int(j) % 10 ** (1 + data.index(i)))
    return result

print(From8([1234]))