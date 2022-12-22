def PrefSeparate(big, small):
    pref = big[:len(big) - len(small) - 1]
    return pref, big[len(big) - len(small) - 1:], "0" + small

def SortByAsk(first, second):
    for i in range(len(first)):
        if int(first[i]) > int(second[i]):
            return False, first, second
        elif int(first[i]) < int(second[i]):
            return False, second, first
    return True, first, second

def FindDiff(big, small):
    result, addiction = "", False
    for i in range(len(big) - 1, -1, -1):
        if not addiction:
            diff, addiction = DoSubtract(big[i], small[i])
        elif big[i] == "0":
            diff, addiction = DoSubtract("9", small[i])
            addiction = True
        else:
            diff, addiction = DoSubtract(str(int(big[i]) - 1), small[i])
        result = diff + result
    return result

def DoSubtract(first, second):
    # print(first, second)
    result = int(first) - int(second)
    if result < 0:
        result += 10
        addiction = True
    else:
        addiction = False
    return str(result), addiction

def BigMinus(s1, s2):
    pref = ""
    if len(s1) - len (s2) < 0:
        pref, s1, s2 = PrefSeparate(s2, s1)
    elif len(s1) - len(s2) > 0:
        pref, s1, s2 = PrefSeparate(s1, s2)
    else:
        equalNumbers, s1, s2 = SortByAsk(s1, s2)
        if equalNumbers:
            return "0"
    result = FindDiff(s1, s2)
    while result[0] == "0":
        result = result[1:]

    return pref + result

print(BigMinus("1200034", "1023499"))