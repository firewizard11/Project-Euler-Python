t_one = 1
t_two = 2
sum = 0

while t_one < 4000000:
	if t_one % 2 == 0:
		sum += t_one

	temp = t_one + t_two
	t_one = t_two
	t_two = temp
	
print(sum)
