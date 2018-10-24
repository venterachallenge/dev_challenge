import json
# this program takes the old format json file and converts it to the new format given in the readme
# I did leave the variable order the same in order to match with the data transformed in the json file so that
# either file could be run in the solutions.py file with as little trouble as possible
# @pre a Json file named data.json
# @post a Json file named results.json

# set up needed variables for the solution
# default dictionary for storing such things as id vendor and customer id
data = {}
# final json file for solution
json_file = {}
# stores the data for the nested json so it stores quantity, price, item, and revenue
objects = {}
# for syntax reasons we want to know if this is the first Json in the file so we can format it appropriately
isFirst = True

file1 = open('results.json', 'w+')

# for syntax of the output
file1.write("[\n")

# creates a data dictionary to handle the outer values of the json
# then creates a list of dictionaries to handle the actual sales or objects
with open('data.json', 'r') as json_data:
    loaded_json = json.load(json_data)

    for sales in loaded_json:
        # this handles setting up the syntax of the output
        if not isFirst:
            file1.write(",")
        else:
            isFirst = False

        data.update({'id': sales['id']})
        data.update({'vendor': sales['vendor']})
        temp = sales['customer']
        data.update({'customerId': temp['id']})
        # resets variables for the inner iteration
        i = 0
        temp = []

        for items in sales['order']:
            objects = {}
            objects.update({'item': items})
            objects.update({'quantity': sales['order'][items]['quantity']})
            objects.update({'price': sales['order'][items]['price']})
            objects.update({'revenue': sales['order'][items]['quantity'] * sales['order'][items]['price']})
            i += 1
            temp.insert(i, objects)

        data.update({'order': temp})
        json_file = json.dumps(data, indent=4)
        file1.write(json_file)
# again for syntax of the output
file1.write("]\n")
file1.close()
