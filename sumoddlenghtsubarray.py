from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        ans=0
        n=len(arr)
    
        for i in range(n):
            for j in range(i+1,n+1):
                if ((j-i)%2):
                

                    ans += sum(arr[i:j])
        return ans
#========== User's Code Ends Here ==========
def main():
    n=int(input())
    arr=[]
    for i in range(0,n):
        arr.append(int(input()))
    s=Solution()
    output = s.sumOddLengthSubarrays(arr)
    
    print(output)
    
main()