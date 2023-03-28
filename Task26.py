def white_walkers(village):
    count, onlyDigits, finds, prev = 0, False, False, -1
    for i in range(len(village)):
        if village[i].isdigit() and prev == -1:
            prev = int(village[i])
        elif village[i].isdigit() and prev + int(village[i]) == 10 and count == 3:
            count = 0
            finds = True
            prev = int(village[i])
        elif village[i].isdigit() and prev + int(village[i]) == 10:
            prev = int(village[i])
            onlyDigits = True
        elif village[i].isdigit():
            prev = int(village[i])
        if village[i] == "=" and prev != -1:
            count += 1
    return finds and not onlyDigits
