# make a def function
def product(number_one, number_two):
    # use a for loop
    for multiplicand in range(number_one,number_two):
        # use a for loop inside a for loop
        for multiplier in range(number_one,number_two):
            print(multiplicand * multiplier, end=" ")
            print(" ")
    return True

# run the program
product(1, 11)