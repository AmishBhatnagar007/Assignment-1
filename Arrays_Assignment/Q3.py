def revArr(arr):
    for i in range(len(arr)//2):
        k=arr[i]
        arr[i]=arr[len(arr)-i-1]
        arr[len(arr)-i-1]=k
    return arr
print(revArr([2, 4, 5, 7, 9, 12]))