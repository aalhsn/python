"""
Output message, so the user know what is the code about 
and some instructions

Condition_Task 
author: Abdullah Alhasan
"""
print("""
	Welcome to Abdullah's Calculator!
	
	Please choose vaild numbers and an operator to be calculated...

	Calculation example: 
	first number [operation] second number = results

	""")

calc_results = 0

num1= input("Input first number:  ")

try:
	num1 = int(num1)
except ValueError:
	print("Invaild values!")
else:
	num2= input("Now, second number:  ")
	
	try:
		num2 = int(num2)
	except ValueError:
		print("Invaild values!")
	else:
		op = input("""Please type in the operator symbol what is between the [..]:
					[ + ]: Addition
					[ - ]: Substraction
					[ x ]: Multiplying
					[ / ]: Division

					Type here:   """)

	if op == "+":
		results = num1 + num2
		print("""
		{} {} {} = ... 
		answer is {} """.format(num1,op,num2,results))
	elif op == '-':
		results = num1 - num2
		print("""
		{} {} {} = ... 
		answer is {} """.format(num1,op,num2,results))
	elif op.lower() == "x":
		results = num1 * num2
		print("""
		{} {} {} = ... 
		answer is {} """.format(num1,op,num2,results))
	elif op == "/":
		results = num1 / num2
		print("""
		{} {} {} = ... 
		answer is {} """.format(num1,op,num2,results))
	else:
		print("Operator is invaild!")