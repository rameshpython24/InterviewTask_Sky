from collections import namedtuple

#Question 1a
def calculate_square_root(number):
    approximate_root = number/2  # Step 1: start with an approximate root
    quotient = number/approximate_root  # Step 2: divide number by approximate root
    new_approximate_root = (approximate_root + quotient)/2  # Step 3: calculate new approximate root
    while round(new_approximate_root, 6) != round(quotient, 6):  # Step 5: repeat until approximations converge
        approximate_root = new_approximate_root
        quotient = number/approximate_root
        new_approximate_root = (approximate_root + quotient)/2
    return round(new_approximate_root, 6)
    
print("Question 1a Testing \n Sqaure Root of 159 : " ,calculate_square_root(159))

#question 1b
numbers = [159, 3400, 67, 598, 8999]

# create a new list of square roots using square_root_iteration function
square_roots = [calculate_square_root(num) for num in numbers]

print("\n\nQuestion 1b testing \n Sqaure roots of list of numbers given :\n",square_roots)

#Question 1c
# create list of tuples with each number and its square root
SquareRoot = namedtuple('SquareRoot', ['number', 'square_root'])  # namedtuple object
results = [SquareRoot(num,sqrt) for num, sqrt in zip(numbers, square_roots)] # list of named tuples

print("\n\nQuestion 1c testing \n List of named tuples of numbers and squareroots :\n",results)



print("\n =========================================================\n")
#Question 2a
class SquareRoot:                         # inilizing SquareRoot class
    def __init__(self, value, approx_value):      # constructor inilization
        self.value = value
        self.approx_value = approx_value
    
    def calculate_square_root(self):         # method for calculating square root
        approx_value = self.approx_value
        quotient = self.value/approx_value
        new_approx_value = (approx_value + quotient)/2
        while round(new_approx_value, 6) != round(quotient, 6):
            approx_value = new_approx_value
            quotient = self.value/approx_value
            new_approx_value = (approx_value + quotient)/2
        return round(new_approx_value, 6)

print("\n Question  2b testing \n ")
#Question 2b
# create a list of values to calculate the square root of
values = [159, 3400, 67, 598, 8999]


# create a list of SquareRoot objects and calculate the square root for each value
square_roots = []
for value in values:
    approx_value = int(value ** 0.5)  # use integer square root as initial approximation
    root = SquareRoot(value, approx_value)  # object creation
    square_roots.append(root.calculate_square_root()) # calling calculate_square_root method from SquareRoot class and append to list

print(square_roots)

