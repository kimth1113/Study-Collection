arr = [4, 6, 5, 7, 2, 3, 1]

for i in range(len(arr)-1, 0, -1):
    for j in range(0, i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)