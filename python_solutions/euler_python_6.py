'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385.

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 == 55**2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

def euler_6(n):
    # Find the sum of the squares.
    sum_of_squares = 0
    for i in range(1, n + 1):
        sum_of_squares += i**2

    # Find the square of the sums.
    square_of_sum = sum(range(1, n + 1))**2

    # Return the difference.
    return abs(square_of_sum - sum_of_squares)

print(euler_6(100))