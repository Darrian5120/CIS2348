import csv


#user input file name
user_file = str(input())

# open file and read
with open(user_file, 'r') as csvfile:
    input = csv.reader(csvfile, delimiter=',')
    spreadSheet = next(input)

    #create array to store amount of repeating words.
    wordArray = {}

    # loop thru csv and add to countArray
    for words in spreadSheet:
        if words.strip() in wordArray:
            wordArray[words] = wordArray[words] + 1 # if word already exist
        else: 
            wordArray[words] = 1 # add 1 to the array since word is new.

    for word, amount in wordArray.items():
        print(str(word) + ' ' + str(amount))