def Unmanned(L, N, track):
    time, odometer, places = 0, 0, getPlaces(track)
    while odometer < L:
        odometer += 1
        time += 1
        if odometer in places:
            time = w8(time, track[places.index(odometer)])
    return time


def getPlaces(track):
    places = []
    for trLight in track:
        places.append(trLight[0])
    return places


def w8(time, light):
    count = 0
    curr = True
    while count < time:
        if curr:
            count += light[1]
            curr = False
        else:
            count += light[2]
            curr = True
    if curr and (count == time or count > time):
        return time
    elif not curr and count > time:
        return count
    elif not curr and count == time:
        return time
