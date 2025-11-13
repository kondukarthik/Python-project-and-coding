def count():
    f = open("res.txt", 'r')
    w = f.read()
    v = c = u = l = sp = n = s = 0
    for i in w:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
        if i.islower() and i >= 'a' and i <= 'z':
            if i in 'aeiou':
                v += 1
            else:
                c += 1
        elif i >= '0' and i <= '9':
            n += 1
        elif i == ' ':
            sp += 1
        else:
            s += 1
    print("Vowels:", v)
    print("Consonants:", c)
    print("Uppercase:", u)
    print("Lowercase:", l)
    print("Special characters:", s)
    print("Spaces:", sp)
    print("Numbers:", n)

count()
