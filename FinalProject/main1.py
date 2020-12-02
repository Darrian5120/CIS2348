import os
import glob
import xlwt
import xlrd
import csv
import pandas
import pandas as pd
import numpy as np
from collections import defaultdict
import pprint
import datetime
from datetime import date
import operator

class Items:
    def __init__(self, item_id = 0, manfac_name = 'none', item_type = 'none', damage = '', price = 0, date = 'none'):
        self.item_id = item_id
        self.manfac_name = manfac_name
        self.item_type = item_type
        self.damage = damage
        self.price = price
        self.date = date
    
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
        for j in range(lines):
            if (item[i][0] == x[j][0]):
                item[i].append(x[j][1])

if __name__ == "__main__":
    lines = 0
    for row in open('ManufacturerList.csv'):
        lines += 1
    
    item = [] 
    prices = []
    dates = []

##################### Create list of lists ########################
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
    
#################### Create full inventory CSV file ####################
    with open('FullInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(finalized_items)

################## Create past service Inventory CSV file ####################
    past = []
    d1 = datetime.datetime.now()
    for i in range(lines):
        if (datetime.datetime.strptime(finalized_items[i][5],'%m/%d/%Y')<d1):
            past.append(finalized_items[i])

    with open('PastServiceDateInventory.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerows(past)

    
    


#################### create class objects ####################
    objs = list()
    for i in range(lines):
        objs.append(Items())

    for i in range(lines):
        objs[i].item_id = int(finalized_items[i][0])
        objs[i].manfac_name = finalized_items[i][1]
        objs[i].item_type = finalized_items[i][2]
        objs[i].damage = finalized_items[i][3]
        objs[i].price = int(finalized_items[i][4])
        objs[i].date = finalized_items[i][5]

    ## create dicitonary with keys as item_id and values as class objects ##
    item_dict = {}
    for i in range(lines):
        item_dict[objs[i].item_id] = None
    for key in item_dict:
        for i in range(lines):
            if (key == objs[i].item_id):
                item_dict[key] = objs[i] 

