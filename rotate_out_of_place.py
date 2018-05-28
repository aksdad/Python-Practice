
def rotate_sub(i, j, n):
    return j, n - i - 1

def rotate_oop(arr):
    n = len(arr)
    new_arr = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            new_i, new_j = rotate_sub(i, j, n)
            new_arr[new_i][new_j] = arr[i][j]

    return new_arr

def pretty_print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == '__main__':
    arr = [[1,2,3],
           [4,5,6],
           [7,8,9]]
    pretty_print_matrix(rotate_oop(arr))