def hcf(a, b):
    if b == 0:
        return abs(a)
    else:
        return hcf(b, a % b)

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
k = hcf(a, b)
print("HCF:", k)
