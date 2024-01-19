def setZeroes(matrix):
    indices = []
    for index, value in enumerate(matrix):
        if any(x==0 for x in value):
            for inner_index in range(len(value)):
                if value[inner_index] == 0:
                    print(value, value[inner_index])
                    indices.append(inner_index)
            matrix[index] = [0] * len(value)
    print(indices)
    for second_index in range(len(matrix)):
        for indic in indices:
            matrix[second_index][indic] = 0
    return(matrix)



if __name__ == '__main__':
    #matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    matrix1 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(setZeroes(matrix1))