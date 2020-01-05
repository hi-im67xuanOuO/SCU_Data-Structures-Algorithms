def matrixElementsSum(matrix):
    # For
    # matrix = [[0, 1, 1, 2], 
    #          [0, 5, 0, 0], 
    #          [2, 0, 3, 3]]
    # the output should be matrixElementsSum(matrix) = 9.
    x = 0
    for i in range(len(matrix[0])): #0,1,2
        for j in range(len(matrix)): #0,1
            if matrix[j][i]!=0:
                x += matrix[j][i]
            else:
                break
    return x

