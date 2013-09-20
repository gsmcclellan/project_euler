"""Greg McClellan
   Created: 8/4/13
   Last Updated: 8/4/13

   Program reads a file containing a large number. Calculates the largest
   number equal to the product of 5 consecutive digits"""

def read_number(file_name):
    #opens a text file to read a large number, returns that number as a list of
    #its digits as integers
    with open(file_name, "r") as textfile:
        number = textfile.read()
        number = list(number)
        number_minus_newline = []
        
        for num in number:
            if not(num == '\n'):
                number_minus_newline.append(int(num))
                
    return number_minus_newline

def calc_product(list_name, list_index):
    #Takes a list and an index number, returns the product of 5 consecutive
    #items in that list starting with the item at list_index
    product = list_name[list_index] * list_name[list_index+1] * \
              list_name[list_index+2] * list_name[list_index+3] * \
              list_name[list_index+4]
    return product

def find_biggest_product(list_name):
    #Takes a list and returns the biggest number obtained from the product
    #of five consecutive numbers in that list
    biggest_product = 0
    
    for i in range(len(list_name) - 4):
        x = calc_product(list_name, i)
        if(x > biggest_product):
            biggest_product = x

    return biggest_product

number = read_number("Largest_product_in_a_series.txt")
biggest_product = find_biggest_product(number)
print(biggest_product)

