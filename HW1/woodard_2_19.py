#Darrian Woodard
#1593984

lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
# FIXME (1): Finish reading other items into variables, then output the three ingredients
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
servings = float(input('How many servings does this make?\n'))

print('\nLemonade ingredients - yields', "{:.2f}".format(servings), 'servings')
print("{:.2f}".format(lemon_juice_cups),'cup(s) lemon juice')
print("{:.2f}".format(water_cups), 'cup(s) water')
print("{:.2f}".format(agave_nectar_cups), 'cup(s) agave nectar\n')

# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
servings2 = float(input('How many servings would you like to make?\n'))
factor = servings2 / servings
print('\nLemonade ingredients - yields', "{:.2f}".format(servings2), 'servings')
print("{:.2f}".format(lemon_juice_cups * factor), 'cup(s) lemon juice')
print("{:.2f}".format(water_cups * factor), 'cup(s) water')
print("{:.2f}".format(agave_nectar_cups * factor), 'cup(s) agave nectar\n')

# FIXME (3): Convert and output the ingredients from (2) to gallons
print('Lemonade ingredients - yields', "{:.2f}".format(servings2), 'servings')
print("{:.2f}".format(lemon_juice_cups * factor / 16), 'gallon(s) lemon juice')
print("{:.2f}".format(water_cups * factor / 16), 'gallon(s) water')
print("{:.2f}".format(agave_nectar_cups * factor / 16), 'gallon(s) agave nectar')
