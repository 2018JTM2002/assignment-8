m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
matrix = []; columns = []
# initialize the number of rows
for i in range(0,m):
  matrix += [0]
# initialize the number of columns
for j in range (0,n):
  columns += [0]
# initialize the matrix
for i in range (0,m):
  matrix[i] = columns
for i in range (0,m):
  for j in range (0,n):
    print ('entry in row: ',i+1,' column: ',j+1)
    matrix[i][j] = int(input())
print (matrix)
