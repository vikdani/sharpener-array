def find_minimum(arr, length):
    """Function to find the minimum in the array 
    return the minimum value"""
    
        minimum=arr[0]
        for i in range(1,length):
            if minimum>arr[i]:
                minimum=arr[i]
        return minimum 
        
    
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_minimum(arr, n))
    
main()

    