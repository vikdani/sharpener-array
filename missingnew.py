from typing import List
class Solution:
    def missing_elements(self, arr):
        
        arr.sort()
        n=len(self.arr)+1
        sum1=0
        while n>0:
            sum1=sum1+n
            n=n-1
        sum2=sum(self.arr)
        return sum1-sum2  
    
      
ob=Solution()
ob.missing_elements(1)    
n=int(input("enter"))
arr=[]
print("enter element")
for i in range(0,n):
    l=int(input())
    arr.append(l)