def MatrixTurn(Matrix, M, N, T):
    matrix = [[0 for j in range(N)] for i in range(M)]
    for i in range(M):
        for j in range(N):
            matrix[i][j] = Matrix[i][j]
    for count in range(T):
        for C in range(int(min(M, N) / 2)):
            temp = matrix[0 + C][0 + C]
            for i in range(1 + C, N - C):
                temp, matrix[0 + C][i] = matrix[0 + C][i], temp
            for i in range(1 + C, M - C):
                temp, matrix[i][N - 1 - C] = matrix[i][N - 1 - C], temp
            for i in range(N - 2 - C, - 1 + C, - 1):
                temp, matrix[M - 1 - C][i] = matrix[M - 1 - C][i], temp
            for i in range(M - 2 - C, - 1 + C, - 1):
                temp, matrix[i][0 + C] = matrix[i][0 + C], temp
    for i in range(M):
        Matrix[i] = ""
        for j in range(N):
            Matrix[i] += matrix[i][j]
