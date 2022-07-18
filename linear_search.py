def linear_search(list, target):
    #returns the target positin if found else returns none

    for i in range(0, len(list)):
        if list[i] == target:
            return i 

    return None

def verify(index):
    if index is not None:
        print("target found at position :", index + 1)
    else:
        print("target not found")

numbers = [ 1,2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 3)

verify(result)

