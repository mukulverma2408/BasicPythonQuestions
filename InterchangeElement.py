#Python program to interchange first and last elements in a list

def SwapElement(lst):
    #print(lst[0], lst[-1])
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst = [14, 15, 23, 45,83]
print(SwapElement(lst))
