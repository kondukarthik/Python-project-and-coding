import re
def vph(ph):
    pat = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(re.match(pat,ph))

def ve(em):
    pat = re.compile(r'^[a-zA-Z0-9]+@[gmail]+\.[com]')
    return bool(re.match(pat,em))

usph=input("Enter ph:")
usem=input("Enter em:")

phv=vph(usph)
emv=ve(usem)

if phv and emv:
    print("Both are right")
elif phv:
    print("ph right")
elif emv:
    print("em right")
else:
    print("Both are wrong")