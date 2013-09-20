"""
	Greg McClellan
	Created: 8/23/2013
	Last Edited; 8/23/13

	Project reads a file containing a 20x20 grid of two-digit numbers. Returns the largest product of
	four connected numbers either vertically, horizontally or diagonally.
"""
def read_grid(file_name):
	#Opens the text file and reads grid, stores it as a 20x20 matrix of ints
	grid = []
	with open(file_name, "r") as textfile:
		for i in range(20):
			line = textfile.readline()
			line = line.split()
			grid.append(line)

	for i in range(20):
		for j in range(20):
			grid[i][j] = int(grid[i][j])

	return grid

def get_product(grid, position):
	#Calculates 4 products starting with the number in the grid at given position.
	#One horizontal, on vertical, and two diagonal to the right and left.
	#Returns the largest product
	products = []

	if grid[position[0]][position[1]] == 0:
		return 0

	#Vertical product
	if position[0] < 17:
		products.append(grid[position[0]][position[1]] * grid[position[0] + 1][position[1]] * \
			grid[position[0] + 2][position[1]] * grid[position[0] + 3][position[1]])

	#Horizontal product
	if position[1] < 17:
		products.append(grid[position[0]][position[1]] * grid[position[0]][position[1] + 1] * \
			grid[position[0]][position[1] + 2] * grid[position[0]][position[1] + 3])

	#Diagonal-right product
	if position[0] < 17 and position[1] < 17:
		products.append(grid[position[0]][position[1]] * grid[position[0] + 1][position[1] + 1] * \
			grid[position[0] + 2][position[1] + 2] * grid[position[0] + 3][position[1] + 3])

	#Diagonal-left product
	if position[0] < 17 and position[1] > 2:
		products.append(grid[position[0]][position[1]] * grid[position[0] + 1][position[1] - 1] * \
			grid[position[0] + 2][position[1] - 2] * grid[position[0] + 3][position[1] - 3])

	if not products:
		return 0

	return sorted(products)[::-1][0]

def get_largest_product(file_name):
	grid = read_grid(file_name)

	largest_product = 0

	for i in range(len(grid)):

		for j in range(len(grid[1])):
			x = get_product(grid, [i, j])

			if x > largest_product:
				largest_product = x

	return largest_product

print(get_largest_product("Largest_Product_In_A_Grid.txt"))