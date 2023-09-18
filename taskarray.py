def prime_numbers(n):
    """ Function to store first n prime_numbers in a list
    Return the list containing the prime numbers """
    
   

    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
def get_first_n_primes(n):
        primes = []
        i = 2
        while len(primes) < n:
            if prime_numbers(i):
                primes.append(i)
            i+= 1
        return primes 
   
    primes = get_first_n_primes(n)    
    
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
