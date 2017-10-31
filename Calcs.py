#simple_Calc

def add(x, y):
	return x + y
def less(x, y):
	return x - y
def multiply(x, y):
	return x * y
def divition(x, y):
	return x % y
print ("Select the Option")
print ("1.Add")
print ("2.Less")
print ("3.Multiply")
print ("4.Divition")

choice = raw_input ("Enter choice(1/2/3/4):")

num1 = (raw_input("Enter the First Value:"))
num2 = (raw_input("Enter the Second Value:"))
try:
 	
	if choice == "1":
		print (num1,"+", num2, "=", add(num1,num2))
	elif choice == "2":
		print (num1, "-",num2, "=", less(num1,num2))
	elif choice == "3":
		print (num1, "*", num2, "*", multiply(num1,num2))
	elif choice == "4":
		print (num1, "%", num2, "%",divition(num1,num2) )
	else:
		print (" *** Invalid Input *** ")
except ValueError:
		print (" *** Invalid Input *** ")
