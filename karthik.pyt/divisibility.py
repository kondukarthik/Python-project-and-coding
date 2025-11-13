def minimum_moves_to_divisible(a, b):
    remainder = a % b
    moves = 0 if remainder == 0 else b - remainder
    return moves

def main():
    t = int(input())

    for _ in range(t):
        a, b = map(int, input().split()) 
        moves = minimum_moves_to_divisible(a, b)
        print(moves) 

if __name__ == "__main__":
    main()
