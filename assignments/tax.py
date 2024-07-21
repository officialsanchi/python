TEN_PERCENT = 0.10
FIFTHEEN_PERCENT = 0.15
TWENTY_PERCENT = 0.2
TWENTY_FIVE_PERCENT = 0.25


cost = int (input("Ask for the price of car and show  : "))

if cost  <= 1000000:
	cost * TEN_PERCENT
	
elif cost > 1000000 and cost <= 3000000:
	cost * FIFTHEEN_PERCENT = 0.15

elif cost > 3000000 and cost <= 5000000:
	cost * TWENTY_PERCENT = 0.2

else: 
	cost > 5000000
	cost * TWENTY_FIVE_PERCENT = 0.25


	