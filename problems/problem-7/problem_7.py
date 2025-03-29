import math


def is_prime(n: int) -> bool:
	n_root = int(math.sqrt(n))

	for i in range(2, n_root+1):

		if n % i == 0:
			return False

	return True


def list_n_primes(n: int) -> list[int]:
	primes = []
	cur_num = 2

	while len(primes) < n:

		if is_prime(cur_num):
			primes.append(cur_num)

		cur_num += 1

	return primes


if __name__ == '__main__':
	n = 10001 
	result = list_n_primes(n)
	print(result[-1])
