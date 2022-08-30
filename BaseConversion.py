# Numbers base conversion

# Write a function that takes two integers (x and b) as inputs
# and returns a string that represents the number x in base b 

def baseConversion(a, b):
    if (a // b) == 0:
        return str(a)
    return baseConversion(a // b, b) + str(a % b)


# Examples:
# If x=5 and b=2 then the function will return "101" 
print(baseConversion(5, 2))
# If x=5 and b=3 then the function will return "12" 
print(baseConversion(5, 3))
