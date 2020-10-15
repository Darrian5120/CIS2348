#Darrian Woodard
#1593984

my_list = str(input())
int_list = my_list.split()
map_object = map(int, int_list)

new_list = list(map_object)
new_list.sort()

for i in range(len(new_list)):
    if new_list[i] >= 0:
        print(new_list[i], end=' ')