import datetime
from datetime import date
#this code will help separate the variabels of today's date

today= date.today()
today_yr = today.year
today_mnth = today.month
today_day = today.day

age_yr = 0
age_mnth = 0
age_d = 0 
birth_date = 0
user_age = 0
user_age_all = 0
user_age_years = 0
user_age_months = 0
user_age_days = 0

def check_birthdate(year,month,days):
		if year > today_yr:
			return False
		elif year == today_yr and month > today_mnth:
			return False
		elif year == today_yr and month == today_mnth and days > today_day:
			return False 
		else:
			return True
def calculate_age(yearb,monthb,daysb):
	birth_date = datetime.datetime(yearb,monthb,daysb)
	user_age = (datetime.datetime.now() - birth_date)
	user_age_all = int(user_age.days)
	user_age_years = int(user_age_all / 365.25)
	user_age_months = int((user_age_all % 365.25) / 30.4168)
	user_age_days = round((user_age_all % 365.25) % 30.4168)
	print("You are {} years, {} months, and {} days old!".format(user_age_years,user_age_months,user_age_days))


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