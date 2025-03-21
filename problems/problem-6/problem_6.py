def sum_of_squares(n: int) -> int:
    total = 0
    for i in range(1, n+1):
        total += (i**2)
    return total

def square_of_sum(n: int) -> int:
    total = sum(list(range(1, n+1))) ** 2
    return total

if __name__ == '__main__':
    n = 100

    x = sum_of_squares(n)
    y = square_of_sum(n)

    print(abs(x - y))