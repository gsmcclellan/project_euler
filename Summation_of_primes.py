"""Greg McClellan
   Created: 8/4/13
   Last Edited: 8/4/13

   Program calculates the sum of all primes below a certain value
"""
from math import sqrt

def check_prime(number):
    #Takes a number as input and returns true if that number is prime
    #or false if not
    if number <= 1:
        return false
    
    for i in range(2, int(sqrt(number)) + 1):
        if number % i == 0:
            return False

    return True

def get_next_prime(prime):
    #Takes a prime number and returns next largest prime number
    while(prime > 0):
        
        if(prime < 2):
            return 2
        elif(prime % 2 == 0):
            prime += 1
        elif(prime % 2 == 1):
            prime += 2
        if(check_prime(prime)):
            return prime

def list_of_primes(upper_limit):
    #returns a list of all primes less than upper_limit
    list_of_primes_ = [x for x in range(1, upper_limit) if x%2 == 1 and \
                      sqrt(x) != int(sqrt(x))] #all odds and non-squares
    list_of_primes_.insert(0, 2)

    for num in list_of_primes_:
        if not(check_prime(num)):
            list_of_primes_.remove(num)
        else:
            print(num)

    return list_of_primes_

def sum_of_primes(upper_limit):
    #returns sum of all primes below upper_limit
    sum_of_primes = 0
    prime = 2 #first prime number
    batch = int(sqrt(upper_limit))
    current_batch = batch
    count = 0

    while(prime < upper_limit):
        batch_sum = 0

        while(prime <= current_batch and prime < upper_limit):
            batch_sum += prime
            prime = get_next_prime(prime)

        sum_of_primes += batch_sum
        current_batch += batch
        count += 1
        print("Batch # %i: Adding %i to sum" %(count, batch_sum), \
              "\nCurrent total is %i" %(sum_of_primes), \
              "\nCurrent prime is %i" %(prime))

    return sum_of_primes

            
"""        
        for x in range(1, upper_limit, batch):
            count += 1           
            batch_sum = 0
            
            for x in range(1, batch):
                prime = get_next_prime(prime)
                if(prime > upper_limit):
                    break
                batch_sum += prime

            sum_of_primes += batch_sum
            print("Batch #%i: %i" % (count, batch_sum))
            print("Sum = %i, current prime is %i" % (sum_of_primes, prime))
"""

upper_limit = 2000000
total = sum_of_primes(upper_limit)
print("Sum of all primes less than %i equals %i" %(upper_limit, total))
