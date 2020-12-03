import os
import glob
import csv
import datetime
from datetime import date
from datetime import datetime 
import operator

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
        x.append(row)
        row_num+=1
    for i in range(lines):
        for j in range(lines): #if prices or dates missing change lines to range(len(x))
            if (item[i][0] == x[j][0]):
                item[i].append(x[j][1])

if __name__ == "__main__":
    lines = 0
    for row in open('ManufacturerList.csv'):
        lines += 1
    
    item = [] 
    prices = []
    dates = []

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

    finalized_items = sorted(item, key =lambda l:l[1], reverse=False)
    for i in range(lines):
        finalized_items[i].append(finalized_items[i].pop(3))

#################### Create full inventory CSV file ##########################
    with open('FullInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(finalized_items)

################## Create past service Inventory CSV file #####################
    past = []
    d1 = datetime.now()
    for i in range(lines):
        if (datetime.strptime(finalized_items[i][4],'%m/%d/%Y')<d1):
            past.append(finalized_items[i])
    past = sorted(past, key =lambda x: datetime.strptime(x[4],'%m/%d/%Y'))
    with open('PastServiceDateInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(past)

#################### Create damaged inventory list #############################
    damaged = []
    for i in range(lines):
        if (finalized_items[i][5] == 'damaged'):
            damaged.append(finalized_items[i])
    damaged = sorted(damaged, key =lambda l:l[3], reverse=True)   
    
    with open('DamagedInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(damaged)

###################### Create Item Type Inventory list #########################
    typeList = []
    files = []
    amt = 0
    filename = '{}Inventory.csv'
    for i in range(lines):
        if finalized_items[i][2] not in typeList:
            typeList.append(finalized_items[i][2])
            files.append(filename.format(finalized_items[i][2]))
            amt+=1
    
    fullFiles = [[] for i in range(amt)]

    for i in range(amt):
        for j in range(lines):
            if (typeList[i] == finalized_items[j][2]):
                fullFiles[i].append(finalized_items[j])
    
    
    for i in range(amt):
        fullFiles[i] = sorted(fullFiles[i], key=lambda l:l[0], reverse=False)
        with open(files[i], 'w', newline='') as f:
            write = csv.writer(f)
            write.writerows(fullFiles[i])

#################### create class objects ######################################
    objs = list()
    for i in range(lines):
        objs.append(Items())

    for i in range(lines):
        objs[i].item_id = int(finalized_items[i][0])
        objs[i].manfac_name = finalized_items[i][1]
        objs[i].item_type = finalized_items[i][2]
        objs[i].price = int(finalized_items[i][3])
        objs[i].date = finalized_items[i][4]
        objs[i].damage = finalized_items[i][5]

    ## create dicitonary with keys as item_id and values as class objects ##
    item_dict = {}
    for i in range(lines):
        item_dict[objs[i].item_id] = None
    for key in item_dict:
        for i in range(lines):
            if (key == objs[i].item_id):
                item_dict[key] = objs[i] 

############################### Menu ###########################################
    command = ''
    while(command != 'q'):
        manfac_type = str(input('Enter manufacturer or q to quit:\n'))
        if (manfac_type == 'q'):
            command = 'q'
            break
        user_list = manfac_type.split()
        user_list = user_list[-2:]
        
        user_items = [] # list ofr all items with matching manfac & type
        service_check = [] # list of items with no service past due
        in_inv = False
        for value in item_dict.values():
            if ((value.manfac_name.lower() == user_list[0].lower()) and (value.item_type.lower() == user_list[1].lower())):
                in_inv = True
                user_items.append(value)
        print('All items {}'.format(user_items))
        if (in_inv == False):
            print('No such item in inventory')
        elif (in_inv == True):
            for i in range(len(user_items)):
                if ((datetime.strptime(user_items[i].date,'%m/%d/%Y')>d1) and user_items[i].damage == ''): # may have to change .date to [4]
                    service_check.append(user_items[i])
        print('All service items {}'.format(service_check))   
        most_expensive = service_check[0]
        for i in range(len(service_check[0:-1])):
            if (service_check[i].price > service_check[i+1].price):
                most_expensive = service_check[i]
        print('most_expensive {}'.format(most_expensive))
        
        print('Your item is: {}'.format(most_expensive))


