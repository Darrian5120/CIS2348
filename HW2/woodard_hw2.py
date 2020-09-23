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

#Extract data from string
month = user_bday.find(' ', 0)
monthNum = user_bday[0:month]

day = user_bday.find(',', month)
dayNum = user_bday[month+1:day]

last_int = month + day

yearNum = user_bday[day+2:last_int]

month_int = 0

#change month string to int
for month_num, month_str in month_dict.items():
    if month_str == monthNum:
        month_int = month_num

print('{}/{}/{}'.format(month_int, dayNum, yearNum))
