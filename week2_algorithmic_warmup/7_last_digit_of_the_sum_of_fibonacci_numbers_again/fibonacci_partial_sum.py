# Uses python3
import sys
from math import sqrt

def fibonacci_number(n):
    if n <= 1:
        return n

    result = (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n) // sqrt(5)

    return result

def fibonacci_partial_sum_naive(from_, to):
    from_sum = fibonacci_number(from_ + 2) - 1
    to_sum = fibonacci_number(to + 2) - 1
    _sum = to_sum - from_sum
    return _sum % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
