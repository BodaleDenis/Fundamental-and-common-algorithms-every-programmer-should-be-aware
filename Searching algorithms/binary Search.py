"""
    Name: Binary Search
    Performance(worst-case): O(log n)
    Performance(best-case):  O(1)
    Data type: Array with an already sorted data
    Summary: As name suggest is an algorithm used for searching through sorted data in a array.
    The idea behind this algorithm is to split searching space by moving left/right on the array 
    depending on the value you are searching for. So in this case your space of search is halved with each iteration.
"""
def binarySearch(element, dataList):
    left = 0
    right = len(dataList) - 1

    while left <= right:

        middle = (left + right) // 2

        if element > dataList[middle]:
            left = middle + 1

        elif element < dataList[middle]:
            right = middle - 1

        else:
            print("Element found")
            return middle
    print("Element not found")
    return None

def binarySearchRecursive(element, dataList, left, right):

    if left <= right:
        middle = (left + right) // 2

        if dataList[middle] is element:
            print("Element found")
            return middle
        elif element > dataList[middle]:
            return binarySearchRecursive(element, dataList, middle + 1, right)
        else:
            return binarySearchRecursive(element, dataList, left, middle - 1)
    else:
        print("Element not found")
        return None
    

#Driver code
inputList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

binarySearch(5, inputList) # Element found
binarySearch(19, inputList) # Element found
binarySearch(22, inputList) # Element not found

binarySearchRecursive(23, inputList, 0, len(inputList) - 1) # Element found
binarySearchRecursive(11, inputList, 0, len(inputList) - 1) # Element found
binarySearchRecursive(30, inputList, 0, len(inputList) - 1) # Element not found
    
