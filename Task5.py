def SynchronizingTables(N, ids, salary):
    if N > 1:
        seq = []
        for i in ids:
            seq.append(i)

        def sort(N, spis):
            i, j = 0, 0
            while i < N:
                while j < N:
                    if spis[j] < spis[i]:
                        spis[i], spis[j] = spis[j], spis[i]
                    j += 1
                i += 1
                j = i + 1
            return spis
        salary = sort(N, salary)
        seq = sort(N, seq)

        def re(m1, m2, m3):
            if m1 != m3:
                for i in m2:
                    for j in m1:
                        if j == m3[m2.index(i)] and m1.index(j) != m2.index(i):
                            m3[m2.index(i)], m3[m1.index(j)] = m3[m1.index(j)], m3[m2.index(i)]
                            m2[m2.index(i)], m2[m1.index(j)] = m2[m1.index(j)], m2[m2.index(i)]
                re(m1, m2, m3)
            return m2
        return re(ids, salary, seq)
    return salary
