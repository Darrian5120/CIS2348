#Darrian Woodard
#1593984

word = input()
password = ''

for i in range(0, len(word)):
    if word[i] == 'i':
        password += '!'
    elif word[i] == 'a':
        password += '@'
    elif word[i] == 'm':
        password += 'M'
    elif word[i] == 'B':
        password += '8'
    elif word[i] == 'o':
        password += '.'
    else:
        password += word[i]

password = password + "q*s"
print(password)