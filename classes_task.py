import sys
from datetime import date
import time

normal_emp_list = []
manager_list = []
user3 = ''
user4 = ''

class Employee:

	def __intit__(self,name,age,salary,emplyment_date):
	
		self.name = name
		self.age = age
		self.salary = salary
		self.emplyment_date = emplyment_date

	def __str__(self):
		return 

	def get_working_years(self,emplyment_date):
		today = date.today()
		result = today.year - int(emplyment_date)
		return result

class Manager(Employee):
	def __intit__(self, name, age, salary,emplyment_date,bonus_percentage):
		Employee.__intit__(self,name,age,salary,emplyment_date)

		self.bonus_percentage = bonus_percentage

	def get_bonus(self,bonus_percentage,salary):
		return round(((bonus_percentage/100) * salary),3)


def show_list(list_name):
	if list_name == manager_list:
		print("--- MANAGERS LIST ---")
		for a in list_name:
			print ("Name: {}, Age: {}, Salary: {} KWD, Working Years: {}, (BONUS: {} KWD)".format(a.name, a.age, a.salary, a.get_working_years(a.emplyment_date), a.get_bonus(a.bonus_percentage, a.salary)))

	else:
		print("--- EMPLOYEES LIST ---")
		for a in list_name:
			print ("Name: {}, Age: {}, Salary: {} KWD, Working Years: {}".format(a.name, a.age, a.salary, a.get_working_years(a.emplyment_date)))

def add_emp(class_name):

		emp = class_name()

		emp.name = input("Name: ")
		try:
			emp.age = int(input("Age: "))
			emp.salary = float(input("Salary: "))
		except ValueError:
			print("Invaild Entry")
		else:
		
			try:
				if class_name == Manager:
				 	emp.bonus_percentage= int(input("Bonus Percentage (%): "))
				 	emp.emplyment_date= int(input("Empolyment Year: "))
				else:
					emp.emplyment_date= int(input("Empolyment Year: "))
			except ValueError:
				print("Invaild Entry")
			else:
				print("ADDED!")
				if class_name == Manager:
					manager_list.append(emp)
				else:
					normal_emp_list.append(emp)

while True:
	try:
		user_input = int(input("""

	SUSHI & Co. Data Entry Program
	===============================
	ACTIONS AVAIABLE TO HR EMPLOYEE:

	Type number 1 for.. SHOW all Employees 
	Type number 2 for.. SHOW all Managers
	Type number 3 for.. ADD an Employee
	Type number 4 for.. ADD a Manager
	Type number 5 for.. EXIT PROGRAM

	...>"""))

	except ValueError:
		print("Invaild Entry")
	else:
		if user_input == 1:
			show_list(normal_emp_list)
			continue
		elif user_input == 2:
			show_list(manager_list)
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

		else:
			print("""
				Invaild input! TRY AGAIN

				""")
