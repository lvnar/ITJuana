# Squares generator

# Write a generator that takes a number N and returns 
# all perfect squares less than N.

def squares(n):
    a = 1
    while a ** 2 <= n:
        yield a ** 2
        a += 1


# Example: 
# N=30 then the generator will give 1, 4, 9, 16, 25 sequentially 
print(list(squares(30)))
