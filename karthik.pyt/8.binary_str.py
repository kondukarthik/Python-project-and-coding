def generate_bs(n):
    if n == 0:
        return['']
    else:
        return[digit + bitstring for digit in '01' for bitstring in generate_bs(n - 1)]
print(generate_bs(3))