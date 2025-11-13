a = list(map(int, input().split()))
m = 0

def biggest(data, m):
    minus = []
    for i in data:
        if i >= m:
            m = i
        else:
            continue
    for i in data:
        if i != m:
            minus.append(i)
        else:
            continue
    minus.reverse() 
    for i in minus:
        print(m - i, end=" ")

biggest(a, m)
