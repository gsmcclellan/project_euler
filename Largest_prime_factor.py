def check_prime(number):
    """Takes a number as input and returns true if that number is prime
    or false if not"""
    if number <= 1:
        return false
    
    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def get_factors(number):
    """Takes a number as input and returns a list of that number's factors"""
    factors = []
    
    for i in range(1, number):
        if number % i == 0:
            factors.append(i)
            
    return factors

def is_factor(factor, number):
    """Takes 2 numbers as input and returns true if factor is a factor of number
    and false if not"""
    if number % factor == 0:
        return True
    else:
        return False

def next_biggest_factor(current_factor, number):
    """Takes a number and its current biggest factor, and returns the next
    biggest factor"""
    divisor = int(number / current_factor)
    for i in range(divisor + 1, number):
        if number % i == 0:
            return int(number / i)

def largest_prime(number):
    """Takes a number as input and returns that number's largest prime factor"""
    biggest_factor = number
    while biggest_factor > 1:
        print("checking factor: ", biggest_factor)
        if check_prime(biggest_factor):
            print( "found prime")
            return biggest_factor
        else:
            print(biggest_factor, " is not prime")
            biggest_factor = next_biggest_factor(biggest_factor, number)
            print("next biggest factor is ", biggest_factor)
    else:
        return False

x = 600851475143
y = 13195
print(largest_prime(x))

        
