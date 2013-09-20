"""
	Greg McClellan
	Created: 8/23/2013
	Last Edited: 8/23/2013

	Problem: 

	The sequence of triangle numbers is generated by adding the natural numbers. 
	So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	Let us list the factors of the first seven triangle numbers:

	 1: 1
	 3: 1,3
	 6: 1,2,3,6
	10: 1,2,5,10
	15: 1,3,5,15
	21: 1,3,7,21
	28: 1,2,4,7,14,28
	We can see that 28 is the first triangle number to have over five divisors.

	What is the value of the first triangle number to have over five hundred divisors?

"""
from math import sqrt

def factors(number):
	#Returns how many factors the given number has
	factors = 0
	for i in range(1, int(sqrt(number) + 1)):
		if number % i == 0:
			factors += 1

	factors = factors * 2

	if sqrt(number) == int(sqrt(number)):
		factors -= 1

	return factors

def highly_divisible(num_of_factors):
	#Returns the first triangular number that has more factors than the input given as 'num_of_factors'
	num = 0
	add_num = 1

	while (factors(num) <= num_of_factors):
		num += add_num
		add_num += 1

	return num

print(highly_divisible(500))