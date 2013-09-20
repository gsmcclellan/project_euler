""" Max Path Sum 1
	Greg McClellan
	9/6/2013

	Problem:

	By starting at the top of the triangle below and moving to adjacent numbers 
	on the row below, the maximum total from top to bottom is 23.

	   3
	  7 4
	 2 4 6
	8 5 9 3

	That is, 3 + 7 + 4 + 9 = 23.

	Find the maximum total from top to bottom of the triangle below:

	              75
	             95 64
	            17 47 82
	           18 35 87 10
	          20 04 82 47 65
	         19 01 23 75 03 34
	        88 02 77 73 07 63 67
	       99 65 04 28 06 16 70 92
	      41 41 26 56 83 40 80 70 33
	     41 48 72 33 47 32 37 16 94 29
	    53 71 44 65 25 43 91 52 97 51 14
	   70 11 33 28 77 73 17 78 39 68 17 57
	  91 71 52 38 17 14 91 43 58 50 27 29 48
	 63 66 04 68 89 53 67 30 73 16 69 87 40 31
	04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

	NOTE: As there are only 16384 routes, it is possible to solve this problem 
	by trying every route. However, Problem 67, is the same challenge with a 
	triangle containing one-hundred rows; it cannot be solved by brute force, 
	and requires a clever method! ;o)
"""


def read_triangle(file_name):
	"""Reads triangle from a given filename and returns as array"""
	with open(file_name) as textfile:
		triangle = []
		last = False
		while not last:
			line = textfile.readline()
			if line:
				triangle.append(line.split())
			else:
				last = True

	for i, row in enumerate(triangle):
		for j, number in enumerate(row):
			triangle[i][j] = int(number)

	return triangle


def max_path_sum(triangle, position=[0,0], path_sum=0,):
	"""Finds largest sum found by adding numbers from top to bottom row"""
	path_sum += triangle[position[0]][position[1]]

	# If next line is last line, returns sum with greater of two ending numbers
	if position[0] + 2 == len(triangle):
		a = path_sum + triangle[position[0]+1][position[1]]
		b = path_sum + triangle[position[0]+1][position[1]+1]
		if a > b:
			return a
		else:
			return b

	else:
		a = max_path_sum(triangle,
						 position=[position[0]+1,position[1]],
						 path_sum=path_sum)
		b = max_path_sum(triangle,
						 position=[position[0]+1,position[1]+1],
						 path_sum=path_sum)

		if a > b:
			return a
		else:
			return b


def main():
	triangle = read_triangle('Max_path_sum2.txt')
	path_sum = max_path_sum(triangle)
	print(path_sum)


if __name__ == '__main__':
	main()