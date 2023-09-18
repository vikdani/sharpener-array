   
class solution(object):
    def runningSum(self,nums):
            self.nums=nums
            nt=len(self.nums)
            ans=[]
            for i in range(0,nt):
                ans.append(0)
            ans[0]=self.nums[0]
            for i in range(1,nt):
                ans[i]=ans[i-1]+self.nums[i]
            return ans

    n=int(input("enter num"))
    lt=[]
    print("enter the values")
    for i in range(0,n):
        lt.append(int(input())) 
    tp=runningSum(lt,5)
    print(tp)             

       