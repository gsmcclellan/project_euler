""" Amicable Numbers
	Greg McClellan
	9/7/2013

	Problem:

	Let d(n) be defined as the sum of proper divisors of n (numbers less than
	n which divide evenly into n).

	If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
	and each of a and b are called amicable numbers.

	For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
	44, 55 and 110; therefore d(220) = 284. 
	The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

	Evaluate the sum of all the amicable numbers under 10000.
"""
from math import sqrt

def factors(n):
	"""Finds all factors of a number"""
	factors = []
	for number in range(1, int(sqrt(n))+1):
		if n%number == 0:
			if number < sqrt(n):
				factors.append(number)
				factors.append(n//number)
			elif number == sqrt(n):
				factors.append(number)

	return factors


def d(n):
	"""Sum of proper divisors of n"""
	divisors = factors(n)
	return sum(divisors[:-1])


def amicable_pairs(upper_limit=10000, lower_limit=1):
	"""Calculates the sum of all amicable numbers from lower_limit to upper_limit, exclusive"""
	amicable_sum = 0
	for n in range(lower_limit, upper_limit):
		a = n
		b = d(n)
		if a != b:
			if d(b) == a:
				amicable_sum += a

	return amicable_sum


def main():
	lower, upper = int(input("Enter lower limit: ")), int(input("Enter upper limit"))
	amicable_sum = amicable_pairs(upper, lower)
	print(amicable_sum)


if __name__ == '__main__':
	main()