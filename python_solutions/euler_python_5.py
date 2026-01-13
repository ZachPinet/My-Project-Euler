'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def euler_5(n):
    smallest_num = 0
    i = n  # i should always be a multiple of n.

    # While we have not yet found the number...
    while smallest_num == 0:
        num_found = True
        # Check i against the largest numbers first.
        for m in range(n + 1, 1, -1):
            if i % m != 0:
                i += n  # Continue to iterate i by n.
                num_found = False
                break
        if num_found:
            smallest_num = i

    return smallest_num

print(euler_5(20))