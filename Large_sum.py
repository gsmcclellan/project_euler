"""
	Greg McClellan
	Created: 8/23/2013
	Last Edited: 8/23/13

	Problem:

	Work out the first ten digits of the sum of one-hundred 50-digit numbers contained
	in the file, 'large_sum.txt'
"""

def read_numbers(file_name, lines):
	#Reads the one-hundred 50-digit numbers and stores them as a list of strings.
	numbers = []
	with open(file_name, 'r') as textfile:
		for i in range(lines):
			line = textfile.readline()
			numbers.append(line.rstrip())

	return numbers

def get_sum(file_name, lines):
	#Calls read_numbers() to get numbers, then calculates the sum of all numbers, digit by digit and
	#places them in a string. Function then returns the first 10 digits in sum
	numbers = read_numbers(file_name, lines)
	carry = 0
	sum_of_numbers = ''

	for i in range(-1, -51, -1):
		digit_sum = 0

		for item in numbers:
			digit_sum += int(item[i])

		digit_sum += carry

		sum_of_numbers += str(digit_sum % 10)
		carry = int((digit_sum - (digit_sum % 10))/10)

	if carry:
		sum_of_numbers = sum_of_numbers + str(carry)[::-1]

	return sum_of_numbers[len(sum_of_numbers) - 1: len(sum_of_numbers) - 11: -1]

print(get_sum('Large_sum.txt', 100))