def fibonacci_number(n):
    a = { 0: 0, 1: 1, 2: 1 }
    index = n

    if n <= 2:
        return a[n]

    c = [n]

    while n >= 6:
        c.append(n // 2)
        n = n // 2

    # a[2 * k] = a[k] * (2 * a[k + 1] - a[k])
    # a[2 * k + 1] = a[k + 1] ** 2 + a[k] ** 2
    while len(c) > 0:
        x = c.pop()
        k = x // 2

        if a.get(k) is None:
            c.append(x)
            c.append(k)
            continue

        if a.get(k + 1) is None:
            c.append(x)
            c.append(k + 1)
            continue

        if a.get(x) is None:
            if x % 2 == 0:
                a[x] = a[k] * (2 * a[k + 1] - a[k])
            else:
                a[x] = a[k + 1] ** 2 + a[k] ** 2

    return a[index]

def fibonacci_last_digit(n):
    current = fibonacci_number(n)
    return current % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
