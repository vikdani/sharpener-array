
def sort_array(arr, length):
    """Function to sort the array in descending order
    After sorting return the sorted array """
    
    
   
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                c=arr[i]
                arr[i]=arr[j]
                arr[j]=c
                
    return arr           
  
    
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n=int(input("enter num"))
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    output = sort_array(arr,n)
    for i in range(0,n):
        print(output[i])
    
main()