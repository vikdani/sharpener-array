from typing import List
class Solution:
    def missing_elements(self, arr: List[int]) -> int:




        n = int(input("enter"))
        arr = input() 
        l = list(map(int,arr.split(' ')))
    def missing(): 
        for i in range (len(l)): 

            if l[i+1] != l[i] + 1:
                return l[i] + 1
ob=Solution()
ob.missing_elements()