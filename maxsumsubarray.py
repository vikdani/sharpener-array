def maxsum(arr):
    size=len(arr)
    currsum=0
    maxsofar=arr[0]
    st=0;en=0;poi=0
    for i in range(0,size):
        currsum=currsum+arr[i]

        if(maxsofar<currsum):
            maxsofar=currsum
            st=poi
            en=i

        if currsum<0:
            currsum=0
            poi=i+1

    print("max subarray is", maxsofar)
    print("start index is",st)
    print("end of window",en)
arr=[4,-3,-2,2,3,1,-2,-3,6,-6,-4,2,1]    
maxsum(arr)