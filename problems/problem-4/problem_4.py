def is_palindrome(n: int) -> bool:
    str_n = str(n)
    return str_n == "".join(list(reversed(str_n)))

if __name__ == '__main__':
    pallindromes = []
    for i in range(100, 1000):
        for j in range(i, 1000):
            result = i*j
            if is_palindrome(result):
                pallindromes.append(result)

    print(max(pallindromes))