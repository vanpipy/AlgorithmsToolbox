from math import sqrt

def fibonacci_number(n):
    if n <= 1:
        return n

    result = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) // sqrt(5)

    return result

def fibonacci_sum_squares(n):
    n0 = fibonacci_number(n)
    n1 = fibonacci_number(n + 1)
    _sum = n0 * n1
    return _sum % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
