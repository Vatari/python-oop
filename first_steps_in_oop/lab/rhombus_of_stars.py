def print_row(n, row):
    print(' ' * (n - row), end='')
    print(*['*'] * row)


def print_triangle(n_):
    for row in range(1, n + 1):
        print_row(n_, row)


def print_reversed_triangle(n_):
    for row in range(n - 1, 0, -1):
        print_row(n_, row)


def print_rhombus(n_):
    print_triangle(n_)
    print_reversed_triangle(n_)


n = int(input())

print_rhombus(n)
