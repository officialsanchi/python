from random import randint
script = randint, range(1, 1000)
guessthenumber = int (input("Guess my number between 1 to 1000 with the fewest guesses : "))
while guessthenumber  >= 10:
	if guessthenumber == script:
		print ("congratulations. you guessed the number!")
	elif guessthenumber > script: 
		print ("too high")
	else:
		print("too low guess age")

	