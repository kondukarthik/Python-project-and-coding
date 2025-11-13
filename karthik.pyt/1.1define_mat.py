r=int (input("enter no of rows"))
c=int(input("enter no of columns"))
m=[]

for i in range(r):
    l=[]
    for j in range(c):
        v=int(input())
        l.append(v)
    m.append(l)

for i in range(r):
    for j in range(c):
        print(m[i][j],end=' ')
    print()