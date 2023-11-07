
def sum_diag(matrix):
    j1 = 0
    for i in range(len(matrix)):
        sum_linie = 0
        for j in range(len(matrix[i])):
                sum_linie += matrix[j][i]
        if sum_linie == 6 or sum_linie == 28 or sum_linie == 496 or sum_linie == 8128:
            j1 += 1
        if j1 == i:
            

matrix = [
     [4,3,10],
     [1,2,10],
     [1,1,8]
     ]
print(sum_diag(matrix))