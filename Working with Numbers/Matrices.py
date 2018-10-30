x = [[2, 3, 4], [3, 5, 7], [3, 4, 2]]
y = [[5, 3, 2], [8, 2, 5], [2, 5, 3]]

ans = [[0, 0, 0], [0,0,0], [0,0,0]]
for i in range (len(x)):
    for j in range (len(y[0])):
        for k in range (len(y)):
            ans [i][j] += x[i][k] * y[k][j]

for i in ans:
    print (i)