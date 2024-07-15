score = []
for count in range (4):
	num = int(input("Collect input from user : "))
	score.append(num)	

	sum_values = sum(score)
	average = sum_values / 4

	product = 1
	for num in score:
		product *= num
	


	minimum = min(score)
	maximum = max(score)

print(f"the sum_values is: {sum_values}\n the avereage of the score  is : {average}\n the  product of the score is : {product}\n the minimun of the score is {minimum}\n the maximum of the score is :  {maximum}\n")



	
	

	








