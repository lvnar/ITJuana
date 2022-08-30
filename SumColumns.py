# Sum Columns from data file

# Give a Comma Separated File (csv) and a column number 
# (zero being the left most column) return the sum of all 
# the entries in that column.
# Assume that all the entries in the CSV are numbers. 
# Assume also that there are no column headers. 


from functools import reduce

def sumColumns(filename):
    with open(filename) as data:
        numbers = []

        for line in data:
            numbers.append([int(x) for x in line.split(',')])
        
        return [reduce(lambda x,y: x + y, col, 0) for col in zip(*numbers)]


# Example: if the file looks like this: 
# 1,2,3,4 
# 5,6,7,8 
# 9,10,11,12
# the sum of column 0 will be 1+5+9=15 and the sum of column 2 will be 3+7+11=21
print(sumColumns('input.csv'))