#Darrian Woodard
#1593984

my_list = str(input())
words = my_list.split()
count_list = []

for i in range(len(words)):
    count = 0
    for j in range(len(words)):
        if words[j] == words[i]:
            count+=1
    count_list.append(count)


for i in range(len(words)):
    print(words[i], count_list[i])
