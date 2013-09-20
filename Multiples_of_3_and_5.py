def sum_of_multiples(lower_limit, upper_limit):
    numbers = [x for x in range(lower_limit, upper_limit) if x % 3 == 0 or x % 5 == 0]
    sum = 0

    for num in numbers:
        sum += num

    return sum

sum = sum_of_multiples(1, 1000)
print(sum)
