"""
    Name: Linear Search
    Performance(worst-case): O(n)
    Performance(best-case): O(1)
    Data type: Arrays
    Summary: This algorithm is used for search by sequentialy accesing each element from the array and check if value is
    equal to the value we search. This algorithm performance is worst than binary search but it's very easy to implement this
    and the O(n) complexity shouldn't be a problem with a small data set. It's average performance should be around O(n/2) since
    it's a big chance that your element will be found in the first half of the array.
"""

def searchForElement(element, dataList):
    for i in dataList:
        if i is element:
            print("Element found")
            return True
    print("Element not found")
    return False

inputList = [1, 2, 'three', 56, 90, 'six']

# Driver code
searchForElement(2, inputList) # TRUE
searchForElement('six', inputList) # TRUE
searchForElement(88, inputList) # FALSE

    
