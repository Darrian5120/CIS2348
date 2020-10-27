#Darrian Woodard
#1593984

def get_age():
    age = int(input())
    if (age <= 18) or (age >= 75):
            raise ValueError('Invalid age.')
    # TODO: Raise excpetion for invalid ages
    return age

# TODO: Complete fat_burning_heart_rate() function
def fat_burning_heart_rate(age):
    heart_rate = -1
    heart_rate = 0.7 * (220 - age)
    return heart_rate

if __name__ == "__main__":
    # TODO: Modify to call get_age() and fat_burning_heart_rate()
    #       and handle the exception
    try:
        age = get_age()
        if (age <= 18) or (age >= 75):
            raise ValueError('Invalid age.')
        fbhr = fat_burning_heart_rate(age)
        print('Fat burning heart rate for a {} year-old: {} bpm'.format(age, fbhr))
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')
    