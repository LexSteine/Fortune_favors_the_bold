def Unmanned(L, N, track):
    curRange, ResTime, places = 0, 0, Places(track)
    for i in range(len(places)):
        ResTime += places[i]
        curRange += places[i]
        ResTime = w8(ResTime, track[i])
    ResTime += L - curRange
    return ResTime

def Places(massiv):
    res = []
    for i in range(len(massiv) - 1, 0, -1):
        res.insert(0, massiv[i][0] - massiv[i - 1][0])
    res.insert(0, massiv[0][0])
    return res

def w8(time, light):
    count = 0
    curr = True
    while count < time:
        if curr:
            count += light[1] #skip red
            curr = False
        else:
            count += light[2] #skip green
            curr = True
    if curr and (count == time or count > time):
        return time # + light[1]
    elif not curr and count > time:
        return count
    elif not curr and count == time:
        return time

# print(Places([[3,5,5], [5,2,2], [6,1,1], [9, 3, 3]]))
# print(Unmanned(10, 4, [[3,3,3], [5,2,2]]))

# def isGreen(time, light):
#     count = 0
#     res = True
#     while count < time:
#         if not res:
#             count += light[1]
#             res = False
#         else:
#             count += light[2]
#             res = True
#     return res