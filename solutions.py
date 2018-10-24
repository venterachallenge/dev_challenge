import json
'''
calculates the following when given a json file named data-transformed.json

Total revenue (sum of quantity times price of all items)
Vendor with the most revenue
Quantity of hats sold (items where the key is exactly 'hat')
ID of the customer that bought the most ice in October

the results will be outputted to output.txt
'''

total_revenue = 0
hats_sold = 0
# a dictionary that store the vendor name and the total amount of money spent by that vendor
vendor_money = {}
# a dictionary that stores the customer id related with the amount of ice they bought
customer_id = {}

with open('data-transformed.json', 'r') as json_data:
    loaded_json = json.load(json_data)

    for objects in loaded_json:
        # if the vendor is not in the dictionary of vendors add them to the dictionary
        if not (vendor_money.get(objects['vendor'])):
            vendor_money.update({objects['vendor']: 0})

        # if the customer id is not in the dictionary of vendors add them to the dictionary
        if not (customer_id.get(objects['customerId'])):
            customer_id.update({objects['customerId']: 0})

        # iterate through and perform calculations
        for items in objects['order']:
            total_revenue += items['revenue']
            vendor_money[objects['vendor']] += items['revenue']
            if items['item'] == "ice":
                customer_id[objects['customerId']] += items['quantity']
            if items['item'] == "hat":
                hats_sold += items['quantity']

vendor = max(vendor_money, key=vendor_money.get)
ice_id = max(customer_id, key=customer_id.get)

# this handles all the printing
file1 = open('./output.txt', 'w+')
file1.write('total revenue of sales: $' + repr(total_revenue) + '\n')
file1.write("vendor with the most revenue: " + repr(vendor)[1:-1] + '\n')
file1.write("number of hats sold: " + repr(hats_sold) + '\n')
file1.write("ID of customer that bought the most ice: " + repr(ice_id)[1:-1] + '\n')
file1.close()
