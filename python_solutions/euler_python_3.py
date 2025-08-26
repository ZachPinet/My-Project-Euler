'''
The prime factors of 13195 are 5, 7, 13, and 29.

What is the largest prime factor of the number 600851475143?
'''


# Iterate through potential factors of n.
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        # Dividing n by its smallest factor results in its largest.
        if n % i == 0:  # If n is prime, this will never be True.
            n //= i  
        # Check if every valid i is a factor of n.
        else:
            i += 1
    return n

print(largest_prime_factor(600851475143))