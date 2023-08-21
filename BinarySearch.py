def binarysearch(arr, element):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start )// 2
        print("Middle position is : {}".format(mid))
        print("Middle Element is : {}".format(arr[mid]))
        if arr[mid] > element:
            end = mid - 1
        elif arr[mid] < element:
            start = mid + 1
        elif arr[mid] == element:
            print("========Element Found========")
            return mid
    print("Element Not found in array")
    exit(1)

arr = [8, 12, 16, 19, 23, 27, 29, 48, 71]
print(binarysearch(arr, 48))











