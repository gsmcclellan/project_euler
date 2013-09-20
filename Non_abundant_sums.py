""" Non-Abundant Sums
	Greg McClellan
	2013-9-7

	Problem:

	A perfect number is a number for which the sum of its proper divisors is 
	exactly equal to the number. For example, the sum of the proper divisors 
	of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect 
	number.

	A number n is called deficient if the sum of its proper divisors is less 
	than n and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
	number that can be written as the sum of two abundant numbers is 24. 
	By mathematical analysis, it can be shown that all integers greater than 
	28123 can be written as the sum of two abundant numbers. However, 
	this upper limit cannot be reduced any further by analysis even though it 
	is known that the greatest number that cannot be expressed as the sum of 
	two abundant numbers is less than this limit.

	Find the sum of all the positive integers which cannot be written as the 
	sum of two abundant numbers.
"""


from math import sqrt


def proper_divisors(n):
	"""Finds all proper divisors of a number"""
	factors = []
	for number in range(1, int(sqrt(n))+1):
		if n%number == 0:
			if number < sqrt(n):
				factors.append(number)
				factors.append(n//number)
			elif number == sqrt(n):
				factors.append(number)

	return sorted(factors)[:-1]


def abundant_numbers(upper_limit=14062, lower_limit=12):
	"""Generates abundant numbers in input range"""
	abundant_nums = set()
	for n in range(lower_limit, upper_limit+1):
		if sum(proper_divisors(n)) > n:
			abundant_nums.add(n)

	return abundant_nums


def non_abundant_sums(upper_limit=28123, lower_limit=1):
	"""Finds sum of all numbers that can't be expressed as a sum of two abundant numbers"""
	non_abundant_sum = 0

	for number in range(lower_limit, upper_limit+1):
		abundant_nums = abundant_numbers(int(number/2+.5))

		is_abundant_sum = False
		for num in abundant_nums:
			difference = number - num

			if difference in abundant_nums:
				is_abundant_sum = True
				break

		if not is_abundant_sum:
			non_abundant_sum += number

	return non_abundant_sum



def main():
	x = non_abundant_sums()
	print(x)



if __name__ == "__main__":
	main()