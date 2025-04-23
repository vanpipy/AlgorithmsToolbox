from math import sqrt

def fibonacci_number(n):
    if n <= 1:
        return n

    result = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) // sqrt(5)

    return int(result)

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
