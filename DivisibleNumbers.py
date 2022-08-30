# Divisible numbers

# Write a function that takes two integers (x and y)
# and returns a list of numbers between x and y 
# that are divisible by 5 but not by 7 

def divisible(x, y):
    return [x for x in range(x, y) if (x % 5 == 0) and (x % 7 != 0)]


# Example:
print(divisible(3, 200))