name = input("Enter your name : ")
age = input ("Enter your age : ")
print(f' {name }g {age}')

message = """your fullname is 
chidinma and
your age is 30"""
print(message)


name = input("Enter your name : ")

if name:
	print("your name is : " , name)
	print('hello')
	print('tech blazers')
new_age =int ( input("Enter your age : "))

if new_age >= 0:
	print("you are eligible to make your own decisions" )
	print('hello')
	print('tech blazers')
else:
	print("you are a child")
if new_age >= 18 and new_age <= 45:
	print("you are eligible to make your own decisions" )
	print('hello')
	print('tech blazers')
elif new_age >= 10 and new_age <= 19:
	print("you are a teenager" )
	print('hello')
	print('tech blazers')
elif new_age > 0 and new_age < 13:
	print('you are still a child')
else:
	print("you are still my child")








