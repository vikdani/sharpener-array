def findMissing(arr, N):
   
   

    # create a list of zeroes

    temp = [0] * (N+1)
 

    for i in range(0, N):

        temp[arr[i] - 1] = 1
 

    for i in range(0, N+1):

        if(temp[i] == 0):

            ans = i + 1
 

    #print(ans)
 
# Driver code

#if _name_ == '_main_':
N=len(arr)
n=int(input("enter n"))
arr=[]
print("enter element")
for i in range(0,n):
    l=int(input())
    arr.append(l)

    # Function call

findMissing(arr, N)