def checkdup(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]==arr[j]:
                return "True"
    return "False"

print(checkdup([1, 2, 4, 2, 5, 9]))