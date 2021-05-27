# Given an N-by-N integer matrix, rotate it by 90 degrees
# Try to do it in-place

def rotate(matrix):
    
    maxDepth = int(len(matrix) / 2)

    for d in range(maxDepth):
        for i in range(d, len(matrix) - 1 - d):
            top = matrix[d][i]
            right = matrix[i][len(matrix) - 1 - d]
            bottom = matrix[len(matrix) - 1 - d][len(matrix) - 1 - i]
            left = matrix[len(matrix) - 1 - i][d]
            
            matrix[d][i] = left
            matrix[i][len(matrix) - 1 - d] = top
            matrix[len(matrix) - 1 - d][len(matrix) - 1 - i] = right
            matrix[len(matrix) - 1 - i][d] = bottom

    return matrix


# Define depth as the number of elements from an edge element to a center element
# If N is even, we only go to depth - 1, since there is only a single center element that does not need to be rotated.
# If N is odd, we go to depth.
matrix1 = [[1, 5, 9], [11, 100, 7], [23, 6, 4]]
matrix1Rotated = [[23, 11, 1], [6, 100, 5], [4, 7, 9]]
assert rotate(matrix1) == matrix1Rotated

matrix2 = [[1, 5, 9, 2], [3, 7, 11, 4], [-1, 0, 0, 8], [12, 5, 12, 900]]
matrix2Rotated = [[12, -1, 3, 1], [5, 0, 7, 5], [12, 0, 11, 9], [900, 8, 4, 2]]

assert rotate(matrix2) == matrix2Rotated
