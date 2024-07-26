number = int(input("collect number from the user : "))
if number < 999 and  number < 10000:
	num = number // 10
	rev = number % 10
	num1 = num // 10
	rev1 = num % 10
	result = rev + num1 + rev1

print(result)

	
	