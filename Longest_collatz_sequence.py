"""
	Greg McClellan
	Created: 8/25/2013
	Last Edited: 8/25/13

	Problem:

	The following iterative sequence is defined for the set of positive integers:

	n → n/2 (n is even)
	n → 3n + 1 (n is odd)

	Using the rule above and starting with 13, we generate the following sequence:

	13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
	It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

	Which starting number, under one million, produces the longest chain?

	NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz_length(number):
	#Generates a collatz sequence starting with 'number' and returns the number of terms in sequence.
	count = 1

	while number != 1:
		count += 1

		if number % 2 == 0:
			number = number / 2

		else:
			number = 3 * number + 1

	return count

def longest_collatz_length(upper_limit):
	#Returns a number under 'upper_limit' that has the longest collatz sequence.
	number = 2
	longest = 1

	while number < upper_limit:
		x = collatz_length(number)

		print("number: ", number, " - collatz length: ", x)

		if x > longest:
			longest = x
			starting_number = number

		number += 1

	return starting_number

print(longest_collatz_length(1000000))