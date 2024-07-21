def only_float(count_a , count_b):
	
	if type(count_a ) == float and type(count_b) == float:
		return 2
	elif  type (count_a ) == float or  type(count_b)== float:
		return 1
	elif type (count_a) != float and type (count_b )!= float:
		return 0


print(only_float(2, 3))