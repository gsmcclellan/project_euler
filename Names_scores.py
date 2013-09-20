""" Names Scores
	Greg McClellan
	2013-9-7

	Problem:

	Using names.txt, a 46K text file containing over five-thousand first 
	names, begin by sorting it into alphabetical order. 
	Then working out the alphabetical value for each name, multiply this 
	value by its alphabetical position in the list to obtain a name score.

	For example, when the list is sorted into alphabetical order, COLIN, 
	which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
	So, COLIN would obtain a score of 938 × 53 = 49714.

	What is the total of all the name scores in the file?
"""


CHAR_POINTS = {'A': 1,
			   'B': 2,
			   'C': 3,
			   'D': 4,
			   'E': 5,
			   'F': 6,
			   'G': 7,
			   'H': 8,
			   'I': 9,
			   'J': 10,
			   'K': 11,
			   'L': 12,
			   'M': 13,
			   'N': 14,
			   'O': 15,
			   'P': 16,
			   'Q': 17,
			   'R': 18,
			   'S': 19,
			   'T': 20,
			   'U': 21,
			   'V': 22,
			   'W': 23,
			   'X': 24,
			   'Y': 25,
			   'Z': 26}


def read_names(filename):
	"""Reads given filename to retrieve names data"""
	with open(filename) as textfile:
		names = textfile.read()

	names = names.split(',')
	for i, name in enumerate(names):
		names[i] = name[1:-1]	# Remove quotes from ends of each name

	return sorted(names)


def name_score(name, index):
	"""Calculates a name's individual name score based on its chars and index"""
	char_score = 0
	for char in name:
		char_score += CHAR_POINTS[char]

	return char_score * index


def names_scores_total(names):
	"""Assigns a score to each name and adds to a running sum"""
	names_scores_sum = 0

	for i, name in enumerate(names):
		names_scores_sum += name_score(name, i+1)

	return names_scores_sum



def main():
	names = read_names('names.txt')
	score = names_scores_total(names)
	print(score)


if __name__ == '__main__':
	main()