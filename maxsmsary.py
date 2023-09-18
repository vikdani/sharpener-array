def find_maximum_subarray(arr, length):
    """write the code to find the maximum subarray sum
    only return the maximum sum of the subarray . 
    Both array and size of array is given """
    
    
    maxsub=arr[0]
    cursum=0
    for i in arr:
        if cursum<0:
            cursum=0
        cursum +=i
        maxsub = max(maxsub, cursum)
    return maxsub        

"""Dont change anything below. If changed click on reset."""
def main():
    n = int(input("enter value"))
    arr=[]
    for i in range(n):
        arr.append(int(input()))
    print(find_maximum_subarray(arr, n))
    
main()

    