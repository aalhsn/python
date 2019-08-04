
import time
import locale
import datetime

cashier_dict = {}
cashier_list = []

def add_item(item,price,q):
	cashier_list.append({'name': item,
						'price': price,
						'quantity': q})

def show_receipt():
	print("""

	=========================
	........RECEIPT..........
	=========================
	""")

	time.sleep(2)

	for item in cashier_list:
		total_per_item = int(item['quantity']) * float(item['price'])
		print("{} - Quantity: ({}) - Total: {} KWD".format(item['name'].upper(),item['quantity'],round(total_per_item,3)))

	total = 0

	for value in cashier_list:
		total += (int(value['quantity']) * float(value['price']))

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
