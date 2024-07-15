digits = int (input("Enter five digits number : "))
for count in range (digits):
	num1 = digits // 10000
	rev1 = num1 % 10
	num2 = digits // 1000
	rev2 = num2 % 10
	num3 = digits // 100
	rev3 = num3 % 10
	num4 = digits // 10
	rev4 = num4 % 10
	num5 = digits % 10
	
	
print(rev1  , rev2   , rev3  , rev4  , num5  , end="    ")
	