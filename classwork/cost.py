cost = int (input("Ask for the price of car and show  : "))

if cost  <= 1000000:
	print("the amount a user will pay in road tax 10%")
elif cost > 1000000 and cost <= 3000000:
	print("the amount a user will pay in road tax 15%")
elif cost > 3000000 and cost <= 5000000:
	print("the amount a user will pay in road tax 20%")
else: 
	cost > 5000000
	print("the amount a user will pay in road tax 25%")


	