def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def get_primes(n):
    """
    Returns an array containing the first n prime numbers.
    """
    primes = []
    n = 2
    while len(primes) < n:
        if is_prime(n):
            primes.append(n)
        n += 1
    return primes
def main():
    n=int(input("Enter the numbers of prime number you want to print"))
    is_prime(n)
    get_primes(n)
    for i in range(0,n):
        print(get_primes[i])
    
main()

