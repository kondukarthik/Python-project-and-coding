def che_w(wd):
    f = open('res.txt', 'r')
    w = f.read()
    if wd in w:
        print('yes')
    else:
        print('error')

che_w('hi')
