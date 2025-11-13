def palin(s):
    return s == s[::-1]

s=input()

a=palin(s)
if s:
    print('yes')
else:
    print('no')