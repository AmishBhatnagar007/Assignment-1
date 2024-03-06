def rotation(arr,k):
    for i in range(k):
        m=arr[len(arr)-1]
        for j in range(1,len(arr)):
            arr[len(arr)-j]=arr[len(arr)-(j+1)]
        arr[0]=m
    return arr
print(rotation([1,2,3,4,5,6,7],3))
