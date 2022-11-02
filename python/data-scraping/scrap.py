'''This file is collection of inventory items entered by about 10 different users using Windows, Linux, and
Mac so the spacing, item texts, and even case of the items is completely messed up. The items are
purchased at multiple times in a year and so their cost might fluctuate. Here is what we need from the
data:
Unique Items with sum of the items value and the total count of the item.

Rules:
• You should exclude non items (blank, N/A, etc) and items that are missing the cost should be
skipped.
• Output skipped items (with reason) and the line/row number it is found on.
• Sort the list by Object Name ASC
• Should use functions, not be 1 long script.
• If file name not supplied, gracefully error and exit.

Format of the report
------------------------------------------------
RUN DATE: YYYY-MM-DD
Processed XXX Lines in xx seconds
------------------------------------------------
OBJECT NAME
COUNT: XXX COST:
OBJECT NAME
COUNT: XXX COST:
===== SKIPPED ITEMS ====
XX: OBJECT NAME (reason)'''

import csv
import sys
import time
import re
from datetime import datetime

    # use regular expression to get the item name, cost and qty from the line 
    # and store them in a dictionary
    # line: 'Wheel Square 	 $3.50 	 QTY:   9'
    # item_name: 'wheel_square'
    # cost: 3.50
    # qty: 9
    # item_dict = {'wheel_square': {'count': 9, 'cost': 3.5}}
    # 
    # line: BoxTop 	 $105.68 	 AMT: 	5
    # item_name: 'boxtop'
    # cost: 105.68
    # qty: 5
    # item_dict = {'boxtop': {'count': 5, 'cost': 105.68}}
def parseData(line):
    import re
    item_name = format_item_name(re.search(r'^\w+', line).group())
    cost = format_price(re.search(r'\$\d+\.\d+', line).group())
    qty = re.search(r'QTY:\s+\d+', line).group().split(":")[1].strip()
    item_dict = {}
    item_dict[item_name] = {"count": int(qty), "cost": cost}
    return item_dict



# format item name
def format_item_name(item_name):
    # remove the leading and trailing spaces
    item_name = item_name.strip()
    # replace the space with underscore
    item_name = item_name.replace(" ", "_")
    # convert to lower case
    item_name = item_name.lower()

    return item_name

#format price
def format_price(price):
    return float(price.replace("$", ""))    

# read data from text file
def read_data(file_name):
    global end_time
    global line_count
    global unique_item_list
    global skipped_item_list

    with open(file_name, 'r') as f:
        line_count = 1
        reader = csv.reader(f)
        unique_item_list = []
        skipped_item_list = []

        next(reader, None)  # skip the headers
        for row in reader:
            
            line_count += 1
            
            # You should exclude non items (blank, N/A, etc) and items that are missing the cost should be skipped
            line = row[0]

            # if the line is blank or only contains spaces or tabs, skip it
            if re.match(r'^\s*$', line):
                continue
            

            try:
                # parseData(line)
                # item_name = format_item_name(line.split("\t")[0])
                # cost = format_price(line.split('\t')[1])
                # qty = line.split('\t')[3]

                item_name = format_item_name(re.search(r'^\w+', line).group())
                cost = format_price(re.search(r'\$\d+\.\d+', line).group())
                qty = re.search(r'QTY:\s+\d+', line).group().split(":")[1].strip()


            except:
                skipped_item_list.append(str(line_count) + ": " + line + " ("+ str(sys.exc_info()[1]) +")")
                continue

            #print(str(line_count) +"------>" + item_name + " " + str(cost) + " " + qty + " " + " " + str(row))

            if item_name == '' or cost == '' or qty == '':
                skipped_item_list.append(item_name)
            else:
                item_dict = {}
                item_dict[item_name] = {"count": int(qty), "cost": cost}
                
                # check if any dictionary in the unique_item_list has the same key as the item_dict
                # if yes, add the count and cost
                # if no, add the item_dict to the unique_item_list
                if any(d.get(item_name) for d in unique_item_list):
                    for item in unique_item_list:
                        if item_name in item:
                            item[item_name]["count"] += int(qty)
                            item[item_name]["cost"] += cost
                else:
                    unique_item_list.append(item_dict)


                # Sort the list by Object Name ASC
                unique_item_list.sort(key=lambda x: list(x.keys())[0])


    end_time = time.time()
    
# show the output in the following format
def output_format():
    print("RUN DATE: " + str(datetime.now().strftime("%Y-%m-%d")))
    print("Processed " + str(line_count) + " Lines in " + str(end_time - start_time) + " seconds")
    print("------------------------------------------------")
    
    for item in unique_item_list:
        item_name = list(item.keys())[0]
        print(item_name)
        print("COUNT: " + str(item[item_name]["count"]) + " COST: " + str(item[item_name]["cost"]))
        print("----------")
    print("===== SKIPPED ITEMS ====")
    for item in skipped_item_list:
        print(item)

def main():
    global start_time
    if len(sys.argv) < 2:
        print("Please provide a file name")
        sys.exit(1)
    else:
        file_name = sys.argv[1]

    start_time = time.time()
    read_data(file_name)
    output_format()


if __name__ == "__main__":
    main()

