'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def euler4(n):
    largest_palindrome = 0
    
    # Iterate through products of n-digit numbers that start with 9.
    for i in range((10**(n-1) * 9), (10**(n))):
        # Do it again.
        for j in range((10**(n-1) * 9), (10**(n))):
            # Test the product.
            product = i * j
            if str(product) == str(product)[::-1]:
                largest_palindrome = max(largest_palindrome, product)
    return largest_palindrome

print(euler4(3))