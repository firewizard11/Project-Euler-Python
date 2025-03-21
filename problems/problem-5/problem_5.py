def is_divisible_range(n: int, end: int) -> bool:
    for i in range(1, end + 1):
        if n % i != 0:
            return False
        
    return True


if __name__ == '__main__':
    n = 20
    cur = n

    while True:
        if is_divisible_range(cur, n):
            break
        else:
            cur += 1
            
    print(cur)