def TransformTransform(A, N):
    Result = S(S(A))
    summa = 0
    for i in range(len(Result)):
        summa += Result[i]
    return summa % 2 == 0 and summa !=0


def S(A):
    B = []
    for i in range(len(A)): #N
        for j in range(len(A) - i): #0.5N
            k = i + j
            B.append(max(A[j:k+1])) #N
    return B
