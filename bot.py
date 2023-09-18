from array import *
from typing import List
class solution:
     def missing_elements(self, arr: List[int],N) -> int:
        
            self.arr=arr
            self.N=N
    
            temp = [0] * ((self.N)+1)
            for i in range(0,self.N):

                temp[self.arr[i] - 1] = 1
            for i in range(0, self.N+1):

                if(temp[i] == 0):

                    ans = i + 1
 

            print(ans)
ob=solution()       
arr=array('i',[])

n=int(input("enter number of elements "))


for i in range(n):
    arr.append(int(input("enter element :")))

N=len(arr)

ob.missing_elements(arr, N)