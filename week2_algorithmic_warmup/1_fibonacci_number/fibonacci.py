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

if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
