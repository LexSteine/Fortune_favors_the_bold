def WordSearch(len, s, subs):
    s = s.split()
    result = []
    words = [""]
    words = AddWord(s, words, number, len)
    for i in words:
        print(i)
    result = FindSubs(words, subs, result)

    return result


def AddWord(s, words, 0, dlina):
    for i in s:
        if len(i) > dlina:
            if len(words[number]) >= dlina - 1:
                words.append(i[:dlina])
                number += 1
                if s.index(i) == len(s) - 1:
                    s.append(i[dlina:])
                else:
                    s.insert(s.index(i) + 1, i[dlina:])
            else:
                a = dlina - len(words[number])
                words[number] += " " + i[:a]
                if s.index(i) == len(s) - 1:
                    s.append(i[a:])
                else:
                    s.insert(s.index(i) + 1, i[a:])
        elif len(i) == dlina:
            words.append(i)
            number += 1
        else:
            if len(i) + len(words[number]) > dlina - 1:
                words.append(i)
                number += 1
            else:
                if len(words[number]) == 0:
                    words[number] += i
                else:
                    words[number] += " " + i
    return words


def FindSubs(words, subs, result):
    for i in words:
        if i.find(subs) == len(i) - len(subs):
            if i.find(subs) == 0:
                result.append(1)
            elif i[i.find(subs) - 1] == " ":
                result.append(1)
        elif i.find(subs) == 0 and (i[len(subs)] == " "):
            result.append(1)
        elif i.find(subs) != -1 and i[i.find(subs) - 1] == " " and (i[len(subs)] == " "):
            result.append(1)
        else:
            result.append(0)
    return result
