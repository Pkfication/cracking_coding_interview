'''
Keep Count of the Columns and Rows to be nullified after the first traversal. Nullify them afterwards.
'''

def set_zero(arr):
    rlen = len(arr)
    clen = len(arr[0])
    rows = [False] * rlen
    columns = [False] * clen

    for i in range(rlen):
        for j in range(clen):
            if arr[i][j] == 0:
                rows[i] = True
                columns[j] = True

    for i in range(rlen):
        if rows[i] == True:
            nullify_row(arr, i)

    for i in range(clen):
        if columns[i] == True:
            nullify_column(arr, i)

def nullify_column(arr, column):
    rlen = len(arr)
    for i in range(rlen):
        arr[i][column] = 0

def nullify_row(arr, row):
    clen = len(arr[0])
    for i in range(clen):
        arr[row][i] = 0


def log(arr):
    clen = len(arr[0])
    rlen = len(arr)
    for i in range(rlen):
        for j in range(clen):
            print str(arr[i][j]),
        print
arr = [
    [1,0,3,4],
    [5,6,7,8],
    [9,10,0,12]
]

log(arr)
print
set_zero(arr)
log(arr)
