# Basic Asymptotic Analysis of Functions

# Solution:
# For function1, the algorithm goes like this:
# Calculation: (4 * 5) / 2
# The number of iterations will be 1.

# For function2, the algorithm goes like this:
# Calculation: 1 + 2 + 3 + 4
# The number of iterations will be: 1 + 1 + 1 + 1 = 4

# For function3, the algorithm goes like this:
# Calculation: 1 + (1 + 1) + (1 + 1 + 1) + (1 + 1 + 1 + 1)
# The number of iterations will be: 1 + 2 + 3 + 4 = 10

# So for our functions 1, 2, and 3, the number of iterations will depend upon n (4 in our case):
# Fun1: O(1)
# Fun2: O(n)
# Fun3: O(n^2)
# The above conversions are known as the asymptotic analysis of the algorithm.
# Comparison between function1 and function2:
# Function1 has a constant time complexity O(1), meaning it is more efficient.
# Function2 has a linear time complexity O(n), which increases linearly with n and is less efficient than Function1.
