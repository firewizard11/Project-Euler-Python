import math


def trial_division_test(n: int) -> bool:
	root =	math.ceil(math.sqrt(n))
	
	for i in range(3, root):
		if i % 2 != 0 and n % i == 0:
			return False
	
	return True

def trial_division(n: int) -> list[int]:
	root =	math.ceil(math.sqrt(n))
	factors = []
	for i in range(2, root):
		if (n % i == 0) and trial_division_test(i):
			factors.append(i)
	return factors

if __name__ == '__main__':
	n = 600851475143
	print(trial_division(n)[-1])