def sum(matrix):
    increasing = True

    for row in matrix:
        for i in range(1, len(row)):
            if increasing:
                if row[i] <= row[i - 1]:
                    return False
            else:
                if row[i] >= row[i - 1]:
                    return False
            increasing = not increasing

    return True
m = [
      [1,2,3],
      [6,5,4],
      [7,8,9]
    ]
k = sum(m)
print(k)