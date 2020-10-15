#Darrian Woodard
#1593984

import collections

def menu(player_stuff, od):
    
    menu = ('\nMENU\n'
        'a - Add player\n'
        'd - Remove player\n'
        'u - Update player rating\n'
        'r - Output players above a rating\n'
        'o - Output roster\n'
        'q - Quit\n')

    command = ''

    while(command != 'q'):
        print(menu, end='\n')
        command = input('Choose an option:\n')

        while(command != 'a' and command != 'o' and command != 'd' and command != 'r' and command != 'u' and command != 'q'):
            command = input('Choose an option:\n')

        if command == 'a':
            x = int(input("Enter player a new player\'s jersey number:\n"))
            y = int(input("Enter the player\'s rating:\n"))
            player_stuff[x] = y
            od = collections.OrderedDict(sorted(player_stuff.items()))

        if command == 'o':
            print('\nROSTER')
            for key, value in od.items():
                print('Jersey number: {}, Rating: {}'.format(key, value))

        if command == 'd':
            x = int(input('Enter a jersey number:\n'))
            del player_stuff[x]
            del od[x]

        if command == 'u':
            x = int(input('Enter a jersey number:\n'))
            y = int(input('Enter a new rating for player:\n'))
            player_stuff[x] = y
            od = collections.OrderedDict(sorted(player_stuff.items()))

        if command == 'r':
            y = int(input('Enter a rating\n'))
            print('ABOVE {}'.format(y))
            above_dict = {k:v for k, v in od.items() if v>y}
            for key, value in above_dict.items():
                print('Jersey number: {}, Rating: {}'.format(key, value))

############################################################################################

if __name__ == "__main__":
    player_stuff = {}

    count = 1
    for i in range(5):
        x = int(input('Enter player ' + str(count) +'\'s jersey number:\n'))
        y = int(input('Enter player ' + str(count) +'\'s rating:\n'))
        print('')
        count += 1
        player_stuff[x] = y

    od = collections.OrderedDict(sorted(player_stuff.items()))

    print('ROSTER')
    for key, value in od.items():
        print('Jersey number: {}, Rating: {}'.format(key, value))

    menu(player_stuff, od)




