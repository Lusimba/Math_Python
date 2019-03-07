a = [[2,3], [4,5], [6,7]]
b= [len(a)*[0]]
c = len(a[0])
d = b*c
def Transpose(a,d):
    d = b*c
    e=d
    for i in range(len(a)):
        for j in range(len(a[0])):
            e[j][i] = a[i][j]
    for x in e:
        print(x)
Transpose(a,d)
