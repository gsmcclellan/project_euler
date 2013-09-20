def is_divisible(number, divisor):
    #checks to see if number is divisble by divisor
    if(number % divisor == 0):
        return True
    else:
        return False

def is_divisible_range(number, lower, upper):
    #checks if number is divisible by every number between and including
    #lower to upper
    check = False

    for x in range(lower, (upper + 1)):
        if(is_divisible(number, x)):
            check = True
        else:
            return False

    return check

def next_multiple(larger, smaller):
    #returns next largest number that is a multiple of both numbers
    check = False
    number = larger

    while(check == False):
        if(is_divisible(number, larger) and is_divisible(number, smaller)):
            check = True
        else:
            number += larger

    return number

def find_smallest_multiple(larger, smaller):
    #returns smallest multiple of 2 numbers
    x = larger
    
    while not(is_divisible(x, larger) and is_divisible(x, smaller)):
        x = next_multiple(x, smaller)

    return x

def find_smallest_multiple_range(lower, upper):
    #Finds the smallest number that can be divided evenly by all numbers
    #from a lower limit to an upper limit
    check = False
    number = upper
    current_limit = lower

    for x in range(lower, upper + 1):
        number = find_smallest_multiple(number, x)
        

    return number

print(find_smallest_multiple_range(1, 20))


