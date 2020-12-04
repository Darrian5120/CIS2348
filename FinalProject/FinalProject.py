import os
import glob
import csv
import datetime
from datetime import date
from datetime import datetime 
import operator

# Darrian Woodard
# 1593984
# 12/4/20

class Items:
    def __init__(self, item_id = 0, manfac_name = 'none', item_type = 'none', price = 0, date = 'none', damage = ''):
        self.item_id = item_id
        self.manfac_name = manfac_name
        self.item_type = item_type
        self.price = price
        self.date = date
        self.damage = damage
    
    def __repr__(self):
        return f"""
        {self.item_id}, {self.manfac_name}, {self.item_type}, {self.damage} ${self.price}, {self.date}    
        """

def read_in(x, item):
    reader = csv.reader(f, delimiter=',') # read rows into a dictionary format
    row_num = 1
    for row in reader:
        x.append(row) # add csv row to a list index
        row_num+=1
    for i in range(lines):
        for j in range(lines): #if prices or dates missing change lines to range(len(x))
            if (item[i][0] == x[j][0]): # compare ids to ensure data is added to correct id
                item[i].append(x[j][1])

if __name__ == "__main__":
    lines = 0
    # find amt of rows in csv file
    for row in open('ManufacturerList.csv'):
        lines += 1
    
    item = [] # list for manufacturer
    prices = [] # list for prices
    dates = [] #list for service dates

##################### Create list of lists ################################
    with open('ManufacturerList.csv','r') as f:
        reader = csv.reader(f, delimiter=',') # read rows into a dictionary format
        row_num = 1
        for row in reader:
            item.append(row)
            row_num+=1

    with open('PriceList.csv','r') as f:
        read_in(prices, item)

    with open('ServiceDatesList.csv','r') as f:
        read_in(dates, item)

    finalized_items = sorted(item, key =lambda l:l[1], reverse=False) # sort data by manufacturer
    for i in range(lines):
        finalized_items[i].append(finalized_items[i].pop(3)) # move damage to the end of csv row

#################### Create full inventory CSV file ##########################
    with open('FullInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(finalized_items) # write list to csv

################## Create past service Inventory CSV file #####################
    past = [] # past date list
    d1 = datetime.now() # find current date
    for i in range(lines):
        if (datetime.strptime(finalized_items[i][4],'%m/%d/%Y')<d1): # compare dates
            past.append(finalized_items[i]) # add to the list
    past = sorted(past, key =lambda x: datetime.strptime(x[4],'%m/%d/%Y')) # sort based on dates
    with open('PastServiceDateInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(past)  # write list to csv

#################### Create damaged inventory list #############################
    damaged = []
    for i in range(lines):
        if (finalized_items[i][5] == 'damaged'): # check to see if item is damaged
            damaged.append(finalized_items[i]) # add to the list
    damaged = sorted(damaged, key =lambda l:l[3], reverse=True) #sort based on price
    
    with open('DamagedInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(damaged) # write list to csv

###################### Create Item Type Inventory list #########################
    typeList = [] # empty list of item types
    files = [] # empty list of possible files
    amt = 0 # variable to store amount of types
    filename = '{}Inventory.csv' # filename naming convention
    for i in range(lines):
        if finalized_items[i][2] not in typeList: # add different types to list
            typeList.append(finalized_items[i][2])
            files.append(filename.format(finalized_items[i][2]))
            amt+=1
    
    fullFiles = [[] for i in range(amt)] # create empty list of lists of list ex. [[[],[]],[[],[]]]

    for i in range(amt): # add type as one list, and then add the items as list inside that list
        for j in range(lines):
            if (typeList[i] == finalized_items[j][2]):
                fullFiles[i].append(finalized_items[j])
    
    
    for i in range(amt):
        fullFiles[i] = sorted(fullFiles[i], key=lambda l:l[0], reverse=False) # sort by item id
        with open(files[i], 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(fullFiles[i]) # write list to csv

#################### create class objects ######################################
    objs = list() #Create empty list
    for i in range(lines):
        objs.append(Items()) # add empty objects to list

    # add items to each class object
    for i in range(lines):
        objs[i].item_id = int(finalized_items[i][0])
        objs[i].manfac_name = finalized_items[i][1]
        objs[i].item_type = finalized_items[i][2]
        objs[i].price = int(finalized_items[i][3])
        objs[i].date = finalized_items[i][4]
        objs[i].damage = finalized_items[i][5]

    ## create dicitonary with keys as item_id and values as class objects ##
    item_dict = {} # create empty dict
    for i in range(lines):
        item_dict[objs[i].item_id] = None # add keys w/ no values
    for key in item_dict:
        for i in range(lines):
            if (key == objs[i].item_id): #compare ids
                item_dict[key] = objs[i] # add if ids match

############################### Menu ###########################################
    command = ''
    while(command != 'q'):
        manfac_type = str(input('Enter manufacturer and item type or enter q to quit:\n'))
        if (manfac_type == 'q'):
            command = 'q'
            break
        user_list = manfac_type.split()
        user_list = user_list[-2:] # ignore extra words
        
        user_items = [] # list ofr all items with matching manfac & type
        service_check = [] # list of items with no service past due
        in_inv = False
        # check for matching values and add them to new list of matching values
        for value in item_dict.values():
            if ((value.manfac_name.lower() == user_list[0].lower()) and (value.item_type.lower() == user_list[1].lower())):
                in_inv = True
                user_items.append(value)
        if (in_inv == False):
            print('No such item in inventory')
            continue # jump back to top of loop
        #add to new list wtih no past service dates or damage
        elif (in_inv == True): 
            for i in range(len(user_items)):
                if ((datetime.strptime(user_items[i].date,'%m/%d/%Y')>d1) and user_items[i].damage == ''): # may have to change .date to [4]
                    service_check.append(user_items[i])

        # find most expensive item
        most_expensive = service_check[0]
        for i in range(len(service_check[0:-1])):
            if (service_check[i].price > service_check[i+1].price):
                most_expensive = service_check[i]
        print('Your item is: {}'.format(most_expensive)) # display most expensive item

        # find items with same types diff manfac, no damage, and good service
        similar_items = []
        for value in item_dict.values():
            if ((value.item_type.lower() == user_list[1].lower()) and (datetime.strptime(value.date,'%m/%d/%Y')>d1) and (value.manfac_name.lower() != user_list[0].lower()) and (value.damage == '')):
                similar_items.append(value)
        # find item with closest price
        closest_value = similar_items[min(range(len(similar_items)), key = lambda i: abs(similar_items[i].price-most_expensive.price))]
        print('Similar Items: {}'.format(closest_value))



