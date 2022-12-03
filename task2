def odometer (oksana):
    distance = 0
    j = 0
    time = 0
    timeAll = 0
    for i in oksana:
        if j % 2 == 0:
            speed = i
        else:
            time = i - timeAll
            timeAll = i
            distance += speed * time
        j += 1
    return distance