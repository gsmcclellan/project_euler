"""This program is designed to find the difference between the sum of the squares
   and the square of the sums of the first one hundred natural numbers"""

def list_of_squares(lower, upper):
    #returns a list containing the squares for each number from lower to upper
    return [x**2 for x in range(lower, upper+1)]

def sum_of_squares(lower, upper):
    #returns the sum of the squares of each number from lower to upper
    squares = list_of_squares(lower, upper)
    sum_of_squares = 0

    for number in squares:
        sum_of_squares += number

    return sum_of_squares

def square_of_sum(lower, upper):
    #returns the square of the sum of all numbers from lower to upper
    sum_of_numbers = sum(range(lower, upper+1))
    square = sum_of_numbers**2
    return square

def sum_square_difference(lower, upper):
    difference = square_of_sum(lower, upper) - sum_of_squares(lower, upper)
    return difference

print(sum_square_difference(1, 100))
