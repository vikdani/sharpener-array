def isprime(num):
    
    for i in range(2,num):
        if num%i==0:
            return False
        
    return 

    
def prime(n):            
    num=2
    while n:
        if isprime(num):
            yield num
            n=n-1
        num=num+1
    return   
n=int(input("enter :"))  
it=prime(n)
for e in prime(n):
    print(e)
    