def SherlockValidString(s):
    d = RepeatsCount(WordsCount(s))
    if len(d) == 1 or len(d) == 2 and KeyCompare(d):
        return True
    else:
        return False


def WordsCount(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def RepeatsCount(d):
    dic = {}
    for i in d:
        if d[i] in dic:
            dic[d[i]] += 1
        else:
            dic[d[i]] = 1
    return dic


def KeyCompare(d):
    a = []
    for i in d.keys():
        a.append(i)
    if max(a) - min(a) == 1 and (d[max(a)] == 1 or (min(a) == 1 and d[min(a)] == 1)):
        return True
    else:
        return False
