'''def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# create an empty array
primes = []

# iterate through numbers from 2 to 100
for num in range(2, 101):
    if is_prime(num):
        primes.append(num)

print(primes)'''

def prime_numbers(n):
    """ Function to store first n prime_numbers in a list
    Return the list containing the prime numbers """

    if n <= 1:
        return False
    for i in range(2, i):
                
                if n % i == 0:
                    return False
    return True

prime = []


for i in range(2,n):
        if prime(i):
            prime.append(i)


   
"""Dont change anything below. If changed click on reset."""
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
