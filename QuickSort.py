#Quick Sort an array

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        greater = []
        smaller = []
        pivot = arr.pop()
        for i in arr:
            if i > pivot:
                greater.append(i)
            elif i < pivot:
                smaller.append(i)

        return(quicksort(smaller) + [pivot] + quicksort(greater))
        #return (smaller + [pivot] + greater)

arr = [6, 1, 5, 2, 3, 10, 56,23, 43, 28, 90]

print(quicksort(arr))
