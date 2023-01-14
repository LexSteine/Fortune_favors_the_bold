def MisterRobot(N, data):
    result, check = TryToOrder(data)
    return check


def TryToOrder(data):
    check = True
    for i in range(1, len(data) - 1):
        if not CheckOrder([data[i - 1], data[i], data[i + 1]]):
            check = False
        elif not (data[i-1] < data[i] < data[i+1]):
            data[i - 1], data[i], data[i + 1] = HackUtility([data[i - 1], data[i], data[i + 1]])
            data, check = TryToOrder(data)
    return data, check


def CheckOrder(chunk):
    for i in range(3):
        if chunk[0] < chunk[1] < chunk[2]:
            return True
        elif chunk[0] < chunk[1] < chunk[2]:
            return False
        else:
            chunk[0], chunk[1], chunk[2] = chunk[1], chunk[2], chunk[0]


def HackUtility(chunk):
    for i in range(3):
        if not (chunk[0] < chunk[1] < chunk[2]):
            chunk[0], chunk[1], chunk[2] = chunk[1], chunk[2], chunk[0]
        else:
            break
    return chunk
