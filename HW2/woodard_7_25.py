#Darrian Woodard
#1593984

import math


def exact_change(user_total):
    total_dollars = math.floor(user_total / 100)
    user_total %= 100
    qTotal = math.floor(user_total / 25)
    user_total %= 25
    dTotal = math.floor(user_total / 10)
    user_total %= 10
    nTotal = math.floor(user_total / 5)
    user_total %= 5
    pTotal = math.floor(user_total / 1)

    return total_dollars, qTotal, dTotal, nTotal, pTotal


if __name__ == '__main__':
    input_val = int(input())
    if input_val <= 0:
        print("no change")
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)
        if num_dollars == 1:
            print('{} dollar'.format(num_dollars))
        if num_dollars > 1:
            print('{} dollars'.format(num_dollars))
        if num_quarters == 1:
            print('{} quarter'.format(num_quarters))
        if num_quarters > 1:
            print('{} quarters'.format(num_quarters))
        if num_dimes == 1:
            print('{} dime'.format(num_dimes))
        if num_dimes > 1:
            print('{} dimes'.format(num_dimes))
        if num_nickels == 1:
            print('{} nickel'.format(num_nickels))
        if num_nickels > 1:
            print('{} nickels'.format(num_nickels))
        if num_pennies == 1:
            print('{} penny'.format(num_pennies))
        if num_pennies > 1:
            print('{} pennies'.format(num_pennies))



