def SumOfThe(N, data):
    total, counter, i = -1, 0, 0
    while i < N and total != counter:
        for j in range(len(data)):
            if i != j:
                counter += data[j]
        if counter == data[i]:
            total = counter
        else:
            counter = 0
        i += 1
    return total