"""This program will find the 1001st prime number"""

def is_prime(number):
    #Returns True if the number is prime, False if not
    if(number < 2):
        return False

    for i in range(2, number):
        if(number % i == 0):
            return False

    else:
        return True

def get_prime(n):
    #returns the nth prime number
    i = 1
    x = n

    while(i <= n):
        if(is_prime(x)):
            if(i == n):
                return x
            else:
                i += 1
        x += 1
        

print(get_prime(10001))
