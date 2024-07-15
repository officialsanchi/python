amount_invested = int (input(" enter the Amount you want to invest : $ "))
annual_interest = (0.07 * amount_invested)
principal_interest = 0
number_of_years = 1




for count in range(30):
	principal_interest = amount_invested*(1 + annual_interest)**number_of_years
	print(f' interest after {number_of_years} year is ${principal_interest:.6f} ')
	number_of_years += 1 
	
	
	

	


