from collections import Counter

def mcw(fp):
    try:
        with open(fp,'r') as f:
            t = f.read()

        w=t.split()
        mw=Counter(w)
        mw,c = mw.most_common(1)[0]

        return mw,c
    except FileNotFoundError:
        return None, None
    
fp = input()
mw,c=mcw(fp)

if mw is not None:
    print(fp,mw,c)
else:
    print(f"{fp} not found")

