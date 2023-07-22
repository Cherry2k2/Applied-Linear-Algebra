def minor(matrix, row, col):
    
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def determinant(matrix):
    
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for col in range(len(matrix)):
            sign = (-1) ** col
            cofactor = determinant(minor(matrix, 0, col))
            det += sign * matrix[0][col] * cofactor
        return det

def input_matrix():
   
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = float(input(f"Enter the element at position ({i+1}, {j+1}): "))
            row.append(value)
        matrix.append(row)
    return matrix

matrix = input_matrix()

if len(matrix) != len(matrix[0]):
    print("Error: Determinant can only be calculated for square matrices.")
else:
    print("Determinant:", determinant(matrix))
