x = [[1,2,3],
     [3,4,5],
     [5,6,7]]

y = [[1,2,3],
     [4,5,6],
     [6,7,8]]

res = [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        res[i][j] = x[i][j] + y[i][j]
for r in res:
    print(r)