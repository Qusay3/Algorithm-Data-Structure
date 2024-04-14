def linear_serarch(list, target):
    """
    return the index position of target if found, else return None"
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Target found in index: ", index)
    else:
        print("Trarget not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_serarch(numbers, 12)
verify(result)

result = linear_serarch(numbers, 6)
verify(result)