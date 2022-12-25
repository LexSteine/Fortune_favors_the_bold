def MassVote(N, Votes):
    if CheckCountOfWinners(Votes, FindMaxNumber(Votes)) and FindPercent(Votes, FindMaxNumber(Votes)) > "50.000":
        return f"majority winner {Votes.index(FindMaxNumber(Votes)) + 1}"
    elif CheckCountOfWinners(Votes, FindMaxNumber(Votes)) and FindPercent(Votes, FindMaxNumber(Votes)) <= "50.000":
        return f"minority winner {Votes.index(FindMaxNumber(Votes)) + 1}"
    else:
        return "no winner"


def FindMaxNumber(Votes):
    MaxNumber = 0
    for i in Votes:
        if i > MaxNumber:
            MaxNumber = i
    return MaxNumber


def CheckCountOfWinners(Votes, WinNumber):
    Count = 0
    for i in Votes:
        if i == WinNumber:
            Count += 1
    if Count > 1:
        return False
    else:
        return True


def FindPercent(Votes, WinNumber):
    Sum = 0
    for i in Votes:
        Sum += i
    return format(WinNumber / Sum * 100, '.3f')
