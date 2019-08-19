
import time
import datetime

cashier_list = []
name =''
quantity = 0
price = 0.0


print("""


	XYZ Point of Sales (POS) 
	DATE | TIME  {}

                                    by Abdullah Alhasan!


	     """.format(datetime.datetime.now()))

while True:

	name= input("Type Item's Name or 'done' If You Finished..>")

	if name == 'done':
		break
	price = input("Type in Item's Price..>")
	quantity = input("Type Quantity..>")
	cashier_list.append({'name': name,
						'price': price,
						'quantity': quantity})


print("""

=========================
........RECEIPT..........
=========================
""")

time.sleep(1)

total = 0
for item in cashier_list:
	total_per_item = int(item['quantity']) * float(item['price'])
	print("{} (Price per item: {}) - Quantity: ({}) - Total: {}KWD".format(item['name'].upper(),item['price'],item['quantity'],round(total_per_item,3)))
	total += total_per_item

print("""

=========================
GRAND TOTAL: {} KWD

""".format(round(total,3)))