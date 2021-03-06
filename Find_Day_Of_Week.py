""" Find Day of Week
	Greg McClellan
	9/7/2013

	Problem:

	You are given the following information, but you may prefer to do some 
	research for yourself.

	1 Jan 1900 was a Monday.
	Thirty days has September,
	April, June and November.
	All the rest have thirty-one,
	Saving February alone,
	Which has twenty-eight, rain or shine.
	And on leap years, twenty-nine.

	A leap year occurs on any year evenly divisible by 4, but not on a century 
	unless it is divisible by 400.

	Write a Program that asks user for a given date and prints out what
	day of the week that date lies on.
"""
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
		  'July', 'August', 'September', 'October', 'November', 'December']

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

DAYS_OF_MONTHS = {'January': 31,
				  'February': 28,
				  'March': 31,
				  'April': 30,
				  'May': 31,
				  'June': 30,
				  'July': 31,
				  'August': 31,
				  'September': 30,
				  'October': 31,
				  'November': 30,
				  'December': 31}


START_DATE = [1900, 'January', 1]


class Day(object):
	"""Class containing a date and day of week for a given day"""

	def __init__(self, year, month, day, day_of_week=False):
		self.day = day
		self.month = month
		self.year = year
		if day_of_week:
			self.day_of_week = day_of_week
		else:
			self.day_of_week = self.find_day_of_week()

	def __repr__(self):
		return "%i-%s-%i was a %s" %(self.year, self.month, self.day, self.day_of_week)

	def find_day_of_week(self, start):
		"""Calculates day of week based on our given start date"""
		days = self.days_since(start)
		days += DAYS.index(start.day_of_week)
		self.day_of_week = DAYS[int(days%7)]

	def days_since(self, start):
		"""Finds number of days from 'start'"""

		# Find difference of year in days, accounting for leap year
		difference = self.year - start.year
		difference = difference*365.25
		year = self.year - 1
		while difference % 1 > 0:
			if leap_year(year):
				difference = int(difference) + 1
			else:
				difference -= .25
				year -= 1

		# Add difference of month in days, adding leap year check for Feb
		start_month_index = MONTHS.index(start.month)
		self_month_index = MONTHS.index(self.month)
		if start_month_index > self_month_index:
			difference -= 365

		while start_month_index != self_month_index:
			difference += DAYS_OF_MONTHS[MONTHS[start_month_index]]

			# Check for leap year
			if start_month_index == 1 and leap_year(self.year):
				difference += 1

			if start_month_index == 11:
				start_month_index = 0
			else:
				start_month_index += 1


		# Add difference of day
		difference += (self.day - start.day)

		return difference

def leap_year(year):
	"""Determines if current year is a leap year"""
	if year%4 == 0:
		if year%100 == 0:
			if year%400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False



def main():
	reference = Day(1900, 'January', 1, 'Monday')
	day = input("Enter a date (YYYY-MM-DD): ")
	day = day.split('-')
	day = Day(int(day[0]), MONTHS[int(day[1])-1], int(day[2]), 'Monday')
	day.find_day_of_week(reference)

	print(day)


if __name__ == "__main__":
	main()