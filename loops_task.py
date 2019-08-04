
import time
import locale
import datetime

cashier_dict = {}
cashier_list = []

def add_item(item,price,q):
	cashier_list.append([item,price,q])
	cashier_dict[item] = cashier_list.pop()

def show_receipt():
	print("""

	=========================
	........RECEIPT..........
	=========================

	""")
	time.sleep(2)
	for value in cashier_dict.values():
		total_per_item = int(value[2]) * float(value[1])
		print("{} - Quantity: ({}) - Total: {} KWD".format(value[0].upper(),value[2],round(total_per_item,3)))

	total = 0

	for value in cashier_dict.values():
		total += (int(value[2]) * float(value[1]))

	print("""

	=========================
	GRAND TOTAL: {} KWD
	

	

	""".format(round(total,3)))

print("""


	MagicCo. Point of Sales (POS) 
	DATE|TIME {}

                                    powered by me!


	     """.format(datetime.datetime.now()))


while True:

	user_item = input("Enter Item Name or ENTER 'done' when finished:  ")
	if user_item == 'done':
		break
	user_price = input("Enter Price:  ")
	user_q = input("Enter Quantity:  ")

	

	add_item(user_item, user_price, user_q)

show_receipt()
