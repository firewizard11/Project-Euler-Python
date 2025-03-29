def solution(n: int) -> int:
	for a in range(1, n):
		for b in range(a+1, n):
			for c in range(b+1, n):
				if (a**2 + b**2) == c**2 and a + b + c == 1000:
					return a * b * c


if __name__ == '__main__':
	n = 1000
	result = solution(n)
	print(result)
