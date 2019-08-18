import datetime

def check_birthdate(year,month,days):
	today= datetime.datetime.now()
	birthdate= datetime.datetime(year,month,days)

	if birthdate > today:
		return False
	else:
		return True
def calculate_age(yearb,monthb,daysb):
	birth_date = datetime.datetime(yearb,monthb,daysb)
	today= datetime.datetime.now()
	user_age = today - birth_date
	days = user_age.days
	years = days / 365.25
	months = (days % 365.25) / 30.4168 
	day = round((days % 365.25) % 30.4168)
	print("You are {} years, {} months, and {} days old!".format(int(years),int(months),int(day)))


print("""
 Welcome to AgeGenerator!

""")

yr = int(input("Enter year of birth:   "))

mnth = int(input("Enter month of birth:   "))
day= int(input("Enter day of birth:   "))

checker = check_birthdate(yr,mnth,day)

if checker == True:
	calculate_age(yr,mnth,day)
else:
	print("Invaild birthdate.. sorry!")