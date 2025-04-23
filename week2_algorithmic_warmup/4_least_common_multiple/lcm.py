def gcd(a, b):
    while True:
        if b == 0:
            return a

        a0 = b
        b0 = a % b
        a = a0
        b = b0

def lcm(a, b):
    if a == 0 or b == 0:
        return 0

    g = gcd(a, b)
    return (a * b) // g

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

