# Darrian Woodard
#1593984

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

# Class for items
class Items:
    def __init__(self, item_id = 0, manfac_name = 'none', item_type = 'none', damage = False, price = 0, date = 'none'):
        self.item_id = item_id
        self.manfac_name = manfac_name
        self.item_type = item_type
        self.damage = damage
        self.price = price
        self.date = date

        self.items = []

    def getID(self):
       return self.item_id

    # Print object as a string
    def __repr__(self):
        return f"""
        ID: {self.item_id}
        Manufacturer: {self.manfac_name}
        Type: {self.item_type} 
        Damage: {self.damage}
        Price: ${self.price}
        Service Date: {self.date}    
        """
    

""" def concatenate(indir="C:\\Users\\darri\\PycharmProjects\\CIS2348\\FinalProject\\InputFiles", outfile="FullInventory.csv"):
    os.chdir(indir)
    fileList = glob.glob("*.csv")
    dfList = []
    for filename in fileList:
        print(filename)
        df = pandas.read_csv(filename, header = None)
        dfList.append(df)
    concatDf=pandas.concat(dfList, axis=0)
    concatDf.to_csv(outfile, index=None) """

if __name__ == "__main__":
    # TODO - read in each row as a class instance
    # TODO - Read excel rows into class objects, dictionary key = item_id and value = instance of class

    
####################################################################################
    """ values1 = ["item_id", "manfac_name", "item_type", "damage", "price", "date"]
    values2 = ["item_id", "price"]
    values3 = ["item_id", "date"]
    
    df1 = pd.read_csv('ManufacturerList.csv', names=values1)
    df2 = pd.read_csv('PriceList.csv', names=values2)
    df3 = pd.read_csv('ServiceDatesList.csv', names=values3)

    print(df1)

    value1 = df1[["item_id", "manfac_name", "item_type", "damage", "price", "date"]]
    value2 = df2[["item_id", "price"]]
    value3 = df3[["item_id", "date"]]
    dataframes = [value1, value2, value3]

    join = pd.concat(dataframes)

    df = join.to_csv("FullInventory.csv")

    df.groupby('item_id') """

##########################################################################################################
    # Read excel rows into class objects
    #with open('ManufacturerList.csv', 'r') as f:
    #    reader = csv.reader(f)
    #    for row in reader:
    #        items.append(Items(row[0], row[1], row[2], row[3]))
    #     #print([items.item_id for i in items])

##########################################################################################################
    #data = list(csv.reader(open('ManufacturerList.csv')))
    #items = [Items(i, data[1]) for i in data[0:]]
    #print(items[0].item_type)

##########################################################################################################
    #data = list(csv.reader(open('ManufacturerList.csv')))
    #all_items = [Items(i, data[0]) for i in data[1:]] 

##########################################################################################################
    #items = []
    #with open('ManufacturerList.csv', newline='') as csv_file:
    #    reader = csv.reader(csv_file)
        # Unpack the row directly in the head of the for loop.
    #    for item_id, manfac_name, item_type, damage in reader:
            # create instance and append it to the list.
    #        items.append(Items(item_id, manfac_name, item_type, damage))

    #with open('PriceList.csv', newline='') as csv_file:
    #    reader = csv.reader(csv_file)
        # Unpack the row directly in the head of the for loop.
    #    for price in reader:
            # create instance and append it to the list.
    #        items.append(Items(price))
    #print(items[0].price)
##########################################################################################################
    
    # Read content from the manufacturer list file
    item = defaultdict(list) # each value in each column is appended to a list
    with open('ManufacturerList.csv') as f:
        reader = csv.reader(f, delimiter=',') # read rows into a dictionary format
        for row in reader: # read a row as {column1: value1, column2: value2,...}
            for (i,v) in enumerate(row): # go over each column name and value 
                item[i].append(v) # append the value into the appropriate list
                                    # based on column name k

    # Find how many items are in the csv file 
    lines = 0
    for row in open('ManufacturerList.csv'):
        lines += 1

    # assign item_id as keys to a dictionary with no values
    item_dict = {}
    for i in item[0]:
        item_dict[i] = None

    # Create empty objects
    objs = list()
    for i in range(lines):
        objs.append(Items())
        
    # Fill empty objects
    for i in range(lines):
        objs[i].item_id = item[0][i]
        objs[i].manfac_name = item[1][i]
        objs[i].item_type = item[2][i]
        objs[i].damage = item[3][i]
    

    # Read content from the price list file
    prices = defaultdict(list)
    with open('PriceList.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader: 
            for (i,v) in enumerate(row): 
                prices[i].append(v) 
    for i in range(lines):
        for j in range(lines):
            if (objs[i].item_id == prices[0][j]):
                objs[i].price = prices[1][j]

    # Read content from the service date list file
    dates = defaultdict(list)
    with open('ServiceDatesList.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader: 
            for (i,v) in enumerate(row): 
                dates[i].append(v) 
    for i in range(lines):
        for j in range(lines):
            if (objs[i].item_id == dates[0][j]):
                objs[i].date = dates[1][j]

    # Add all object to dictionary values
    for key in item_dict:
        for i in range(lines):
            if (key == objs[i].item_id):
                item_dict[key] = objs[i]
    pprint.pprint(item_dict)
    
    

    
    
    


    #command = ''
    #while(command != 'q'):
    #    manfac = str(input('Enter manufacturer\n'))
    #    item_type = str(input('Enter item type\n'))