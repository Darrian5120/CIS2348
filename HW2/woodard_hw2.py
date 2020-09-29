#Darrian Woodard
#1593984
import re


#Function to make changes to the date
def calc_bday(user_bday):
    #Extract data from string
    month = user_bday.find(' ', 0)
    monthNum = user_bday[0:month]

    day = user_bday.find(',', month)
    dayNum = user_bday[month+1:day]

    last_int = month + day

    yearNum = user_bday[day+2:last_int+1000]

    #month_int = 0

    #change month string to int
    for key, value in month_dict.items():
        if value == monthNum:
            #month_int = key
            return '{}/{}/{}'.format(key, dayNum, yearNum)

    return ''


   
user_bday = str(input())

#month to number dictionary
month_dict = {1: 'January',
              2: 'February',
              3: 'March',
              4: 'April',
              5: 'May',
              6: 'June',
              7: 'July',
              8: 'August',
              9: 'September',
              10: 'October',
              11: 'November',
              12: 'December'
              }

myDates = open('C:/Users/darri/PycharmProjects/CIS2348/HW2/inputDates.txt', 'r')
contents = myDates.readlines()
myDates.close()

#r = re.compile("\\S \\d, \\d")
#if r.match(user_bday) is not None:
print(calc_bday(user_bday), '\n')

with open('C:/Users/darri/PycharmProjects/CIS2348/HW2/parsedDates.txt', 'a') as printedDates:
    for line in range(len(contents)):
        if '/' in contents[line] or '-' in contents[line] or '.' in contents[line]:
            -1
        else:
        #if r.match(contents[line]) is not None:
            print(calc_bday(contents[line]), end='')
            printedDates.write(calc_bday(contents[line]))
