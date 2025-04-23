def gcd(a, b):
    while True:
        if b == 0:
            return a

        a0 = b
        b0 = a % b
        a = a0
        b = b0

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
