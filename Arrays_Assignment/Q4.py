def maxinarr(arr):
    max=0
    for i in range(len(arr)):
        if max<arr[i]:
            max=arr[i]
        else:
            max=max
    return max
print(maxinarr([10, 5, 20, 8, 15]))
        