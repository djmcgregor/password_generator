import numpy as np
import random
import string


def get_input():
    """ Get password settings from user """

    # Define password length
    maximum = int(input('Enter maximum password length: '))
    minimum = int(input('Enter minimum password length: '))
    assert (maximum >= minimum), 'Maximum must be larger than minimum'

    pass_length = random.randint(minimum, maximum)

    # Limit characters
    req = np.zeros(6)
    req[0] = int(input('Enter minimum number of uppercase letters: '))
    req[1] = int(input('Enter minimum number of numbers: '))
    req[2] = int(input('Enter minimum number of special characters: '))
    req[3] = int(input('Enter maximum number of uppercase letters: '))
    req[4] = int(input('Enter maximum number of numbers: '))
    req[5] = int(input('Enter maximum number of special characters: '))
    
    assert (req[3] >= req[0]), 'Max number of uppercase must be >= minimum'
    assert (req[4] >= req[1]), 'Max number of numbers must be >= minimum'
    assert (req[5] >= req[2]), 'Max number of special characters must be >= minimum'
    assert (req[:3].sum() <= pass_length), 'The minimum number of characters exceeds the password length'

    return pass_length, req


def generate_password(pass_length, req):
    """ Create password that meets all user requirements """

    pwd = ""
    count = 0
    l = 0   # lower
    u = 0   # upper
    n = 0   # number
    s = 0   # symbol
    delta = np.zeros(3)

    while count < pass_length:
        delta[0] = req[0] - u
        delta[1] = req[1] - n
        delta[2] = req[2] - s
        del_tot = pass_length - count
            
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        num = random.choice(string.digits)
        symbol = random.choice(string.punctuation)
        everything = ""
        
        pos_sum = delta[delta > 0].sum()
        if pos_sum == del_tot:  #must fill remaining slots with specific chars
            if delta[0] > 0:
                everything += upper
            if delta[1] > 0:
                everything += num
            if delta[2] > 0:
                everything += symbol
        else:                                #Ensure we don't exceed maximums
            everything = lower    
            if u < req[3]:
                everything += upper
            if n < req[4]:
                everything += num
            if s < req[5]:
                everything += symbol
        
        next_char = random.choice(everything)
        pwd += next_char
        count += 1
        if str.islower(next_char):
            l += 1
        elif str.isupper(next_char):
            u += 1
        elif str.isdigit(next_char):
            n += 1
        else:
            s += 1
            
    return pwd


if __name__ == "__main__":
    pass_length, req = get_input()
    pwd = generate_password(pass_length, req)
    print(pwd)
