def half_adder(a, b):
    sum_out = a ^ b
    carry_out = a and b
    return sum_out, carry_out

def full_adder(a, b, cin):
    sum_out1, carry_out1 = half_adder(a, b)
    sum_out2, carry_out2 = half_adder(sum_out1, cin)
    sum_out = sum_out2
    carry_out = carry_out1 or carry_out2
    return sum_out, carry_out

def parallel_adder(a, b):
    n = len(a)
    result = [0] * (n + 1)
    carry = 0
    for i in range(n - 1, -1, -1):
        result[i + 1], carry = full_adder(a[i], b[i], carry)
    result[0] = carry
    return result

a = [1, 0, 1]
b = [0, 1, 0]

hsum, hcarry = half_adder(a[0], b[0])
fsum, fcarry = full_adder(a[0], b[0], 0)
pres = parallel_adder(a, b)

print(hsum, hcarry)
print(fsum, fcarry)
print(pres)
