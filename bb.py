from array import *
class Solution:
    def missing_elements(self,arr,N):
    
        temp = [0] * (N+1)
        for i in range(0, N):

            temp[arr[i] - 1] = 1
        for i in range(0, N+1):

            if(temp[i] == 0):

                ans = i + 1
 

        print(ans)
ob=Solution()        
arr=array('i',[])

n=int(input("enter number of elements "))


for i in range(n):
    arr.append(int(input("enter element :")))

N=len(arr)

ob.missing_elements(arr, N)