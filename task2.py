def odometer(oksana):
    distance, time, i = 0, 0, 0
    while i < len(oksana):
        distance += oksana[i] * (oksana[i + 1] - time)
        time = oksana[i + 1]
        i += 2
    return distance