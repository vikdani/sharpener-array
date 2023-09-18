def is_prime(num):
    """
    Returns True if a number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def get_first_n_primes(n):
    """
    Returns an array of the first n prime numbers.
    """
    primes = []
    i = 2
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1
    return primes