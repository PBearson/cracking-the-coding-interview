# Given an N-by-M matrix, if an element is 0, its entire row and column are set to 0

def setZeroMatrixRowColumn(zeroMatrix, N, M):
    
    for i in range(len(zeroMatrix[0])):
        zeroMatrix[N][i] = True

    for j in range(len(zeroMatrix)):
        zeroMatrix[j][M] = True

def setZeros(matrix):
    zeroMatrix = []

    # initialize Zero matrix
    for i in range(len(matrix)):
        zeroMatrix.append([])
        for j in range(len(matrix[0])):
            zeroMatrix[i].append(False)

    # First find the 0s in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                setZeroMatrixRowColumn(zeroMatrix, i, j)

    # Now set the new 0s in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if zeroMatrix[i][j]:
                matrix[i][j] = 0
    
    return matrix

matrix1 = [[2, 9, 0, 8], [11, 4, 96, 2], [0, 1, 13, 5]]

matrix1Zeroes = setZeros(matrix1)
print(matrix1Zeroes)

matrix2 = [[0, 99, 1000], [4, 27, 1], [17, 26, 4]]
matrix2Zeroes = setZeros(matrix2)
print(matrix2Zeroes)