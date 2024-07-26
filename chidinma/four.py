subtotal = int(input("collect  subtotal from the user : "))
gratuity_rate =int (input("collect gratuity rate from user : "))

gratuity =  (gratuity_rate/100)* subtotal
total = gratuity + subtotal
print (gratuity)
print(total)