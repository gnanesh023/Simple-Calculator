#The Calculater
try:

	input1 = raw_input("Enter the First  Number > ")
	input2 = raw_input("Enter the Second Number > ")


	Sum =float (input1) + float(input2)

	print  ('Your Answer is > {}'.format(Sum))
except ValueError:
	print ("** That's Not a Number **")
