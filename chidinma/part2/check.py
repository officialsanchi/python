index = 2000
for count in range(index, 3000):
	if count % 2 == 0:
		value1 = count % 10
		value2 = count // 10
		value3 = value2 % 10
		value4 = value2 // 10 
		value5 = value4 % 10
		value6 = value4 // 10

		if value1 %2 == 0 and value3 %2 == 0 and value5 %2 == 0 and value6 %2 == 0:
			print(count, end= ' , ')

	
