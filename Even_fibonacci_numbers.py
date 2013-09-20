def create_sequence(upper_limit):
    #Creates a fibonacci sequence containing only even numbers up to
    #a value equaling the input, upper_limit
    sequence = []
    first_term = 1
    previous_term = 1
    current_term = 1
    x = first_term

    while(x <= upper_limit):
        x = previous_term + current_term
        if(x % 2 == 0):
            sequence.append(x)
        previous_term = current_term
        current_term = x

    return sequence

def fibonacci_sum(sequence):
    #Takes input of our even numbered fibonacci sequence and returns the sum
    #of all numbers in the sequence
    fibonacci_sum = 0
    
    for x in sequence:
        fibonacci_sum += x
        
    return fibonacci_sum

print(fibonacci_sum(create_sequence(4000000)))
