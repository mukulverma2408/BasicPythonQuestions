#Python Program to Swap Two Elements in a List

def swapelement(lst, var1, var2):
    lst[var1], lst[var2] = lst[var2], lst[var1]
    return lst

lst = [1,5,2,6,8,10,45,34,98]
var1 = int(input("Enter First element"))
var2 = int(input("Enter element that need to be swapped"))
print("Inital List : ", lst)
print("List after swap is")
print(swapelement(lst, var1, var2))
