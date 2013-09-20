"""
	Greg McClellan
	Created: 8/25/2013
	Last Edited: 8/25/2013

	Problem:

	If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 
	3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
	how many letters would be used?


	NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
	contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
	The use of "and" when writing out numbers is in compliance with British usage.
"""

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

THOUSAND = "thousand"

def number_to_english(number):
	#Takes an integer as input and returns that number as a string of its English written form
   	
	if number < 10:
		return FIRST_TEN[number]

	elif number < 20:
		return SECOND_TEN[number - 10]

	elif number < 100:
		other_ten = int(number/10) - 2
		first_ten = number % 10

		if first_ten > 0:
			return OTHER_TENS[other_ten] + " " + FIRST_TEN[first_ten]
		else:
			return OTHER_TENS[other_ten]

	elif number < 1000:
		if number % 100 > 0:
			return number_to_english(int(number/100)) + " " + HUNDRED + " and " + \
			number_to_english(number % 100)
		else:
			return number_to_english(int(number/100)) + " " + HUNDRED

	else:
		if number % 1000 > 0:
			return number_to_english(int(number/1000)) + " " + THOUSAND + " and " + \
			number_to_english(number % 1000)
		else:
			return number_to_english(int(number/1000)) + " " + THOUSAND

def number_letter_counts(upper_limit, lower_limit = 1):
	#For each number from the given lower limit to upper limit, counts the alpha chars in each number and
	#adds that count to a running total. Returns the total chars for every written number.
	total_letter_count = 0

	for i in range(lower_limit, upper_limit + 1):
		letter_count = 0
		written_number = number_to_english(i)

		for letter in written_number:
			if letter.isalpha():
				letter_count += 1

		total_letter_count += letter_count

	return total_letter_count

def count_letters(number):
	letter_count = 0
	written_number = number_to_english(number)

	for letter in written_number:
		if letter.isalpha():
			letter_count += 1

	return letter_count

#print(number_letter_counts(1000))
print(number_letter_counts(1000))
