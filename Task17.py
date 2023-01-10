def LineAnalysis(line):
    result = True
    line = line.split("*")
    line.pop(0)
    line.pop(len(line) - 1)
    print(line, result)
    for i in line:
        if i != line[0]:
            result = False
            break
    return result
