import sys
from datetime import date
import time

normal_emp_list = []
manager_list = []

class Employee:

	def __init__(self,name,age,salary,emplyment_date):
	
		self.name = name
		self.age = age
		self.salary = salary
		self.emplyment_date = emplyment_date

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s KWD, Working for: %s year(s)" % (self.name,self.age,round(self.salary,3), self.get_working_years())

	def get_working_years(self):
		today = date.today()
		return today.year - int(self.emplyment_date)

class Manager(Employee):
	def __init__(self, name, age, salary,emplyment_date,bonus_percentage):
		Employee.__init__(self,name,age,salary,emplyment_date)
		self.bonus_percentage = bonus_percentage

	def get_bonus(self):
		return round(((self.bonus_percentage/100) * self.salary),3)

	def __str__(self):
		return "Name: %s, Age: %s, Salary: %s KWD, Working for: %s year(s), BONUS: %f KWD" % (self.name,self.age,self.salary, self.get_working_years(), self.get_bonus())


def show_list(list_name):
	if list_name == manager_list:
		for emp in list_name:
			print(emp)
			print(" ")
	else:
		for emp in list_name:
			print(emp)
			print(" ")

def add_emp(class_name):

		name = input("Name: ")
		age = int(input("Age: "))
		salary = float(input("Salary: "))

		if class_name == Manager:
			bonus_percentage= int(input("Bonus Percentage (%): "))
			emplyment_date= int(input("Empolyment Year: "))
			print("ADDED!")
		else:
			emplyment_date= int(input("Empolyment Year: "))
			print("ADDED!")

		if class_name == Manager:
			emp = class_name(name,age,salary,emplyment_date,bonus_percentage)
			manager_list.append(emp)
		else:
			emp = class_name(name,age,salary,emplyment_date)
			normal_emp_list.append(emp)

print("""

	SUSHI & Co. Data Entry Program
	===============================
	ACTIONS AVAIABLE TO HR EMPLOYEE:

	Type number 1 for.. SHOW all Employees 
	Type number 2 for.. SHOW all Managers
	Type number 3 for.. ADD an Employee
	Type number 4 for.. ADD a Manager
	Type number 5 for.. EXIT PROGRAM
	""")

while True:
	try:
		user_input = int(input("(0) for help..>"))

	except ValueError:
		print("Invaild Entry")
	else:
		if user_input == 1:
			print("""
				**********EMPLOYEES LIST**********

				""")
			print(" ")
			show_list(normal_emp_list)
			print("""

				Total: {} employee(s)
				""".format(len(normal_emp_list)))
			continue
		elif user_input == 2:
			print(""""
				_________MANAGERS LIST__________

				""")
			show_list(manager_list)
			print("""

				Total: {} manager(s)
				""".format(len(manager_list)))
			continue
		elif user_input == 3:

			print("""
				[ADDING AN EMPLOYEE]
				""")
			add_emp(Employee)
			continue
		elif user_input == 4:

			print("""
				[ADDING A MANAGER]
				""")
			add_emp(Manager)
			continue
		elif user_input == 5:
			print("CLOSING PROGRAM...")
			sys.exit(0)
		
		elif user_input == 0:

			print("""ACTIONS AVAIABLE TO HR EMPLOYEE:
			Type number 1 for.. SHOW all Employees 
			Type number 2 for.. SHOW all Managers
			Type number 3 for.. ADD an Employee
			Type number 4 for.. ADD a Manager
			Type number 5 for.. EXIT PROGRAM""")
			continue

		else:
			print("""
				Invaild input! TRY AGAIN
				""")
			continue