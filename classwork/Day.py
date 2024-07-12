name = "chidinma"
print (id(name))

name = 'chidinma' + "obioma"
print (id(name))

number = 1
print (id(number))


number = number + 4
print(id(number))

basket = [1,2,3,4,5]
print (id(basket))
basket.append(5)
print(id(basket))
print (basket)

for char in "techblazers":
print "chidinma"

for char in range (100):
print "chidinma"


total = 0
for number in range (1, 101):
	print(number)
if number %2 == 1:
	total += number
	print(total)

result = 0
for number in range (1, 101, 2):
	result += number
	print (result)
value = 0
for number in range (1, 101, -2):
	value += number 