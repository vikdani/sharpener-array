from typing import List


#========== User's Code Starts Here ==========

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max=0
        for i in range(0,len(accounts)):
            row=0
            for j in range(0,len(accounts[i])):
                row=row+accounts[i][j]
            if row>max:
                max=row    

        return max 
#========== User's Code Ends Here ==========
def main():
    n=int(input("enter row"))
    arr=[]
    for i in range(0,n):
        c=int(input("enter column"))
        c_arr=[]
        for j in range(0,c):
            c_arr.append(int(input()))
        arr.append(c_arr)
    s=Solution()
    output = s.maximumWealth(arr)
    
    print(output)
    
main()