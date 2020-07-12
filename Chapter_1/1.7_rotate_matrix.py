'''
To rotate a matrix 90 deg, we transpose the matrix and reverse it columnwise.
'''

def rotate_matrix(a):
    log(arr)
    transpose(arr)
    reverse(arr)
    print
    log(arr)

def log(arr):
    R = C = len(arr)
    for i in range(R):
        for j in range(C):
            print str(arr[i][j]) + " ",
        print

def transpose(arr):
    R = C = len(arr)
    for i in range(R):
        for j in range(i, C):
            t = arr[i][j]
            arr[i][j] = arr[j][i]
            arr[j][i] = t

    return arr

def reverse(arr):
    C = len(arr)
    for i in range(C):
        j,k = 0, C-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1

arr = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ];

rotate_matrix(arr)
