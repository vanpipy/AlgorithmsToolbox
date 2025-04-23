from math import sqrt

def fibonacci_number(n):
    if n <= 1:
        return n

    result = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) / sqrt(5)

    return int(result)

def fibonacci_last_digit(n):
    current = fibonacci_number(n)
    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
