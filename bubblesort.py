def sort_array(arr, length):
    """Function to sort the array in descending order
    After sorting return the sorted array """
    n=len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                temp=arr[j]
                arr[j]=arr[i]
                arr[i]=temp
                
    return arr           

        

    
   
    
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input("enter size"))
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    output = sort_array(arr,n)
    for i in range(0,n):
        print(output[i])
    
main()
