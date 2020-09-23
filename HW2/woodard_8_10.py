#Darrian Woodard
#1593984


def isPalindrome(s):
    return s == s[::-1]

str_check = str(input())
toks = str_check.split(' ')
new_str = ''.join(toks)

if isPalindrome(new_str):
    print('{} is a palindrome'.format(str_check))
else:
    print('{} is not a palindrome'.format(str_check))