'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13. 

What is the 10001st prime number?
'''

def euler_7(n):
    prime_count = 0
    i = 1
    while prime_count < n:
        i += 1
        i_is_prime = True
        # Check if i is divisble by any number half of itself or less.
        for j in range(2, (i // 2) + 1):
            if i % j == 0:
                i_is_prime = False
                break
            
        if i_is_prime:
            prime_count += 1
    return i
        
print(euler_7(10001))