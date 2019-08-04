import time 
skills = ['C++', 'AMPL', 'VDHL', 
		'VBA', 'Python', 'Javascript', 
		'R', 'Text Analyzing', 'Data Analyzing', 
		'Management', 'Cooking', 'Reading', 'Drawing', 
		'Video Editing', 'Photographing']
cv = {}
cv['name'] = input("Enter your name:  ")
	
try:
	cv['age'] = int(input("Enter your age:  "))
	cv['experience'] = int(input("Enter your years of experience:  "))
except ValueError:
	print("Invaild input!")
else:
	cv['skills'] = []
	cv['req'] = False
	req_skills = ['C++', 'Python', 'R', 
				'Text Analyzing', 'Data Analyzing', 
				'Javascript', 'Management']

	def show_help():
		print("""

			* Enter 'DONE' if you are done from adding skills
			* Enter 'SHOW' to show skill set on CV

			* Enter 'HELP' to show those instructions

			""")

	def add_skills(item):
		if item.isdigit() == True:
			item = int(item) - 1
			for skill in skills:
				if skills.index(skill) == item:
					cv['skills'].append(skills[item])
					print("ADDED! Total {} skills on your CV".format(len(cv['skills'])))
		else:
			print("Invaild entry, please enter a number!")

	def show_skills():
		count = 1
		print("Current skills on your CV:")
		for skill in cv['skills']:
			print(count,"- ",skill)
			count += 1
		
	show_help()


	i = 1

	for skill in skills:
		print("[", i, "] ", skill)
		i += 1

	print ("** Choose a skill from the list above by typing in the number (Max. 5 skills):")

	while True:

		user_input = input(">>")
		if user_input == 'DONE':
			break
		elif user_input == 'HELP':
			show_help()
			continue
		elif user_input == 'SHOW':
			show_skills()
			continue
		elif len(cv['skills']) < 5:
			add_skills(user_input)
			continue
		else:
			print("Last entry was not taken! Maximum number of skills reached!")
			break

	show_skills()
	time.sleep(1)
	print("""

		-------------------------------------------------
		We are reviewing your application. Please wait...
		-------------------------------------------------

		""")
	time.sleep(2)

num = 0
for skill in cv['skills']:
	if skill in req_skills:
		num += 1


if cv['age'] < 23 or cv['age'] > 35:
	print("""Dear {}, we had to move on to another candidate. Best of Luck!

		""".format(cv['name']))
	
elif cv['experience'] < 4:
	print("""Dear {}, we had to move on to another candidate. Best of Luck!

		""".format(cv['name']))
elif 'Cooking' not in cv['skills']:
	print("""Dear {}, we had to move on to another candidate. Best of Luck!

		""".format(cv['name']))
elif num < 2 :
	print("""Dear {}, we had to move on to another candidate. Best of Luck!

		""".format(cv['name']))
else:
	print("""Congrats! You have been accepted, {}

		""".format(cv['name']))




