"""
	Greg McClellan
	Created: 8/25/2013
	Last Edited: 8/25/2013

	Problem:

	Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
	there are exactly 6 routes to the bottom right corner.


	How many such routes are there through a 20×20 grid?
"""

from math import factorial

def nCr(n, k):
	return int(factorial(n)/(factorial(k)*factorial(n - k)))

def lattice_paths(n):
	#returns number of paths for an nxn lattice
	return nCr(2*n, n)


print(lattice_paths(20)) 
