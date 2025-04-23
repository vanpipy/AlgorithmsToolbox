# Uses python3
import sys

def fibonacci_number(n):
    if n <= 1:
        return n

    if n == 2:
        return 1

    if n == 3:
        return 2

    i = 2
    a = [0, 1, 1, 2]

    while True:
        next_a_even = a[i] * (2 * a[i + 1] - a[i])
        next_a_odd = a[i] ** 2 + a[i + 1] ** 2
        a.append(next_a_even)
        a.append(next_a_odd)

        if i * 2 == n:
            return next_a_even
        elif i * 2 + 1 == n:
            return next_a_odd

        i += 1

def fibonacci_partial_sum_naive(from_, to):
    from_sum = fibonacci_number(from_ + 2) - 1
    to_sum = fibonacci_number(to + 2) - 1
    _sum = to_sum - from_sum
    return _sum % 10

if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
