'''def nextprime(num):
    while True:
        num=num+1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num

def prime(N):
    num,count=1,1
    while count<=N:
        num=nextprime(num)
        yield num
        count=count+1
N=int(input("how many prime number you want to generate :"))
l=[x for x in prime(N)]
print(l)'''

def prime_numbers(n):
    """ Function to store first n prime_numbers in a list
    Return the list containing the prime numbers """

def nextprime(num):
    while True:
        num=num+1
        for i in range(2,num):
            if num%i==0:
                break
        else:
            return num

def prime_numbers(n):
    num,count=1,1
    while count<=n:
        num=nextprime(num)
        yield num
        count=count+1

#l=[x for x in prime_numbers(n)]

   
    
    
    
    
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
