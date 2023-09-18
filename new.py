def prime_numbers(n):
	result = []
	for cp in range(2,n+1):
		    
		    for i in range (2,cp):
				
				if (cp%i==0):
				    
				    
				    break
				
                else:
		    
		      
    result.append(cp)
	     

	    
	return result

    
   
    
    
def main():
    n=int(input())
    output = prime_numbers(n)
    for i in range(0,n):
        print(output[i])
    
main()
