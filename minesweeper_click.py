
def click(field, num_rows, num_cols, given_i, given_j):
    stack = list()
    stack.append((given_i, given_j))

    while len(stack) > 0:
        row, col = stack.pop()
        if field[row][col] == 0:
            field[row][col] = -2

        for i in range(-1, 2):
            for j in range(-1, 2):
                if row + i >= 0 and row + i < num_rows and col + j >= 0 and col + j < num_cols:
                    if field[row + i][col + j] == 0:
                        stack.append((row + i, col + j))

    return field

def pretty_print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == '__main__':
    field = [[-1,1,0,0],
             [1,1,0,0],
             [0,0,1,1],
             [0,0,1,-1]]

    num_rows = len(field)
    num_cols = len(field[0])
    pretty_print_matrix(click(field, num_rows, num_cols, 1, 1))