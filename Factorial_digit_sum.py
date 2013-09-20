"""
	Greg McClellan
	Created: 8/25/13
	Last Edited: 8/25/13

	Problem: 

	n! means n × (n − 1) × ... × 3 × 2 × 1

	For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
	and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

	Find the sum of the digits in the number 100!
"""

from math import factorial

def factorial_digit_sum(n):
	#returns the sum of digits of n!
	digit_sum = 0
	n = str(factorial(n))

	for digit in n:
		digit_sum += int(digit)

	return digit_sum

print(factorial_digit_sum(100))