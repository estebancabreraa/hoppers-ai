def create_board():
    matrix = [['x', 'x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', 'o'],
              ['x', 'x', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o'],
              ['x', 'x', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
              ['x', 'x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
              ['x', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
              ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'y'],
              ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'y', 'y'],
              ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'y', 'y', 'y'],
              ['o', 'o', 'o', 'o', 'o', 'o', 'y', 'y', 'y', 'y'],
              ['o', 'o', 'o', 'o', 'o', 'y', 'y', 'y', 'y', 'y']]
    return matrix

def print_board(matrix):
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    print ('    1   2   3   4   5   6   7   8   9   10')
    for i in range(0, len(matrix)):
        row = letters[i]
        for o in range(0, len(matrix)):
            row = row + "   " + matrix[o][i]
        print(row)

def transform_pos(pos):
    if (pos.upper() == 'A'):
        return 0
    if (pos.upper() == 'B'):
        return 1
    if (pos.upper() == 'C'):
        return 2
    if (pos.upper() == 'D'):
        return 3
    if (pos.upper() == 'E'):
        return 4
    if (pos.upper() == 'F'):
        return 5
    if (pos.upper() == 'G'):
        return 6
    if (pos.upper() == 'H'):
        return 7
    if (pos.upper() == 'I'):
        return 8
    if (pos.upper() == 'J'):
        return 9

def neighbor(mat, row, col, radius=1):

    rows, cols = len(mat), len(mat[0])
    out = []

    for i in range(row - radius - 1, row + radius):
        row = []
        for j in range(col - radius - 1, col + radius):

            if 0 <= i < rows and 0 <= j < cols:
                row.append(mat[i][j])
            else:
                row.append(0)

        out.append(row)

    return out
