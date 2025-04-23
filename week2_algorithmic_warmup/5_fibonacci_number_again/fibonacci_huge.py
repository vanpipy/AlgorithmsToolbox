def fibonacci_number(n):
    a = { 0: 0, 1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8 }
    index = n

    if n <= 6:
        return a[n]

    c = [n]

    while n // 2 >= 2:
        c.append(n // 2)
        n = n // 2

    while len(c) > 1:
        x0 = c.pop()
        x1 = c[len(c) - 1]
        if x1 % 2 == 0:
            a[x1] = a[x0] * (2 * a[x0 + 1] - a[x0])
        else:
            a[x1] = a[x0] ** 2 + a[x0 + 1] ** 2

    return a[index]

def fibonacci_huge_naive(n, m):
    current = fibonacci_number(n)
    return current % m


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
