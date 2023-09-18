def get_primelist(upper):
	result = []
	for cp in range ( 2, upper + 1 ):
		for i in range ( 2, cp ):
			if ( cp % i == 0 ):
				break
		else:
			result.append(cp)
	return result

# RUN to create an array of the prime numbers
# [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
#  43,47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97 ]
n=int(input("Enter range to print prime numbers"))
print(get_primelist(n))

'''def prime_numbers(n):


    myarr=[]
    for num in range(2,n+1):
        fact=0
        for i in range(2,num):
            if num%i==0:

                fact=1
                break
        if fact==0:
            myarr.append(num)    

    return myarr
   
    
    
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
'''