def remove_duplicates(arr):
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]

    del arr[unique_index + 1:]

    return arr

print(remove_duplicates([1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]))
