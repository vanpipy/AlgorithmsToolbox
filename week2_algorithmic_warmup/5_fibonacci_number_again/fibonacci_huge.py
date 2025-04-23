from math import sqrt

def fibonacci_number(n):
    if n <= 1:
        return n

    result = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) // sqrt(5)

    return int(result)

def fibonacci_huge_naive(n, m):
    current = fibonacci_number(n)
    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
