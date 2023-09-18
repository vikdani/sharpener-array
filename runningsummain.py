from typing import List
#========== User's Code Starts Here ==========
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums    
#========== User's Code Ends Here ==========
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    s=Solution()
    output = s.runningSum(arr)
    string =""
    for i in range(0,n):
        string =string + str(output[i]) +" "
    print(string)
    
main()