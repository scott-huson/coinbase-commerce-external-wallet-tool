import csv
from blockcypher import get_address_overview

print("Starting BTC Scanning Script:")
addresses = []
count = 0
with open('49adds.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	# for i in range(360, 500):
	# 	address = get_address_overview(reader[i][1][1:])
	# 	print(count)
	# 	if(address['balance'] > 0):
	# 		addresses.append(reader[i][0][-5:])
	# 		print("{} Satoshis at {} ({})".format(address['balance'],row[i][1],row[i][0]))

		# address = get_address_overview(row[1][1:])
		# print(count)
		# if(address['balance'] > 0):
		# 	addresses.append(row[0][-5:])
		# 	print("{} Satoshis at {} ({})".format(address['balance'],row[1],row[0]))
		count += 1
	print("Went through", count, "addresses")
for n in addresses:
	print(n)
