def mymax(t):
    n=len(t)
    mx=t[0]
    for i in range(1,n):
        if t[i]>mx:
            mx=t[i]
    return mx
def fmn(t):
    n=len(t)
    p=mymax(t)
    sum1 =(p*(p+1))//2
    sum2=0
    for i in range(0,n):
        sum2 += t[i]
    return sum1-sum2
         
n=int(input("enter n"))
lt=[]
print("enter element")
for i in range(0,n):
    lt.append(int(input()))
tp=fmn(lt)
print("the missing number is :",tp)    