import time


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        print(i)
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(arr)

# Driver code to test above
import time
arr = [3,6,4,8,2,7,5]
start_time = time.time()
insertionSort(arr)
print("waktu")
print((time.time()-start_time)*1000)
