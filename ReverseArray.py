#Simple swapping of array elements using two pointer method

def swaparray(arr):
    if len(arr) <= 1:
        return (arr)
    else:
        newarr = []
        for i in range(len(arr)-1, -1, -1):
            item = arr[i]
            newarr.append(item)
        return(newarr)

arr = [1,5,3,8]

print(swaparray(arr))