
n=int(input("enter numbers of prime number range in between u want to print"))

myarr=[]



for num in range(2,n+1):
    fact=0
    for i in range(2,num):
        if num%i==0:

            fact=1
            break
    if fact==0:
        myarr.append(num)    
print(myarr)
