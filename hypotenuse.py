import math

# Using input() to get user input
side_a = float(input('Enter length of side a: '))
side_b = float(input('Enter length of side b: '))

# Use pow() to square values of a and b
squared_a = math.pow(side_a, 2)
squared_b = math.pow(side_b, 2)

sum_of_squares = squared_a + squared_b

# Use sqrt() to calculate the hypotenuse
hypotenuse = math.sqrt(sum_of_squares)

# Display hypotenuse to two decimal places
print(f"The hypotenuse is: {hypotenuse:.2f}")