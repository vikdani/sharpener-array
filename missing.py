if __name__=='__main__':
    arr=[]
    n=int(input("enter lenght of array"))
    for i in range(n-1):
        m=int(input("enter the element"))
        arr.append(m)

    missingnum=findmissing(arr,n)
    print("the missing number is",missingnum)

