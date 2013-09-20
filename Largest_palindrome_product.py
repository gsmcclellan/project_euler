def check_palindrome(number):
    #Takes a number and returns true if number is a palindrome, false if not
    a = list(str(number))
    b = []
    for item in a:
        b.insert(0, item)
    if(a == b):
        return True
    else:
        return False

def largest_palindrome(digits):
    #Returns the largest palindromic number created by multiplying two numbers
    #with a specified number of digits
    upper_limit = 10**digits - 1
    lower_limit = 10**(digits-1)
    a = upper_limit
    b = upper_limit
    biggest_palindrome = 1
    
    while(a >= lower_limit):
        
        while(b > lower_limit):
            product = a*b
            print("checking product of %i and %i = %i" %(a, b, product))
        
            if(check_palindrome(product)):
                lower_limit = b
                if(product > biggest_palindrome):
                    biggest_palindrome = product
            else:
                b = b - 1
                
        else:
            b = a
            a = a - 1
    return biggest_palindrome

print(largest_palindrome(3))
