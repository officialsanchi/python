import math
def divide_or_square(a_number):
	if a_number % 5 == 0:
		return math.sqrt(a_number)
	else:
		return a_number % 5
print(divide_or_square(10))
print(divide_or_square(7))
print(divide_or_square(25))
print(divide_or_square(49))


