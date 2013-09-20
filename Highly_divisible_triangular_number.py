""" Greg McClellan
    Date Created: unk
    Last Edited: 2013-9-20

        2013-9-20: Added commenting, documentation.
                   Optimized num_of_factors() function.

    Problem: 

    A perfect number is a number for which the sum of its proper
    divisors is exactly equal to the number. For example, the sum of
    the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which
    means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
    smallest number that can be written as the sum of two abundant numbers
    is 24. By mathematical analysis, it can be shown that all integers
    greater than 28123 can be written as the sum of two abundant numbers.
    However, this upper limit cannot be reduced any further by analysis
    even though it is known that the greatest number that cannot be
    expressed as the sum of two abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as
    the sum of two abundant numbers.
"""

from math import sqrt


def num_of_factors(number):
    #Takes an integer as input and returs the number of factors
    count = 0
    for num in range(1, int(sqrt(number)) + 1):
        if number % num == 0:
            if int(sqrt(number)) == sqrt(number):
                count += 1
            else:
                count += 2

    return count
    

def highly_divisible(desired_divisors):
    #Returns the first triangle number with more divisors than the input
    num = 1
    triangle_num = 0
    divisors = 0

    while divisors <= desired_divisors:
        print("Running...")
        triangle_num += num
        num += 1
        divisors = num_of_factors(triangle_num)

    return triangle_num


def main():
    print(highly_divisible(500))


if __name__ == '__main__':
    main()
