"""
	Greg McClellan
	Created: 8/25/2013
	Last Edited: 8/25/2013

	Problem:

	2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

	What is the sum of the digits of the number 2**1000?
"""
def power_digit_sum(base, power):
	#Returns the sum of digits for the number base**number
	number = str(base**power)
	pow_dig_sum = 0

	for digit in number:
		pow_dig_sum += int(digit)

	return pow_dig_sum

print(power_digit_sum(2, 1000))