# function for BS
def binary_search(list,item):
    low = 0;
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2 # int division answer without and remainder
        guess = list[mid]       # guess position is set to mid
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else: low = mid + 1
    return None

my_list = [1,1,2,3,4,5,6,7,8,10]
print (binary_search(my_list,4))
