from typing import List
class Solution:
    def missing_elements(self, arr: List[int]) -> int:
        self.arr=arr
        
        arr.sort()
        n=len(arr)+1
        sum1=0
        while n>0:
            sum1=sum1+n
            n=n-1
        sum2=sum(arr)
        return sum1-sum2    
    def main():
        arr=array('i',[])

        n=int(input("enter number of elements "))


        for i in range(n):
            arr.append(int(input("enter element :")))

b=Solution()
b.missing_elements()        
[1,2,3,4,5]
n=6

sum1=6
n=5
sum1=11
n=4
11=4
15+3
18+2
sum1=21-15
6

