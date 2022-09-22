"""
    Name: Quicksort
    Performance(worst-case): O(N^2)
    Performance(best-case):  O(N*log N)
    Data type: Mostly arrays containing numerical value
    Summary: An sorting algorithm which falls into category of efficient sorting algorithms.
    The main point is to divide dataset in half by selecting middle element and putting all smaller/larger (depends on desired sorting order)
    elements to the left and the oposite to the right, and the process repeats until the comparasion is done between only two elements which means a side
    is already sorted. When one side is sorted it continue to sort the other side.
    Also there are different variations of quicksort which are defined by which element is the pivot (first element, last element, median element or random)
"""
def partition(toSort:list, left_index:int, right_index:int) -> int:
    pivot, pointer = toSort[right_index], left_index
    for i in range(left_index, right_index):
        if toSort[i] <= pivot:
            toSort[i], toSort[pointer] = toSort[pointer], toSort[i]
            pointer += 1
    toSort[pointer], toSort[right_index] = toSort[right_index], toSort[pointer]

    return pointer

def quick_sort(toSort:list, left_index:int, right_index:int) -> list:
    if len(toSort) == 1:
        return toSort
    if left_index < right_index:
        partition_index = partition(left_index, right_index, toSort)
        quick_sort(left_index, partition_index-1, toSort)
        quick_sort(partition_index+1, right_index, toSort)
    return toSort

# Driver code
test_input = [4,5,1,2,3,100,3,20,11,45,67,92]
print(quick_sort(0, len(test_input)-1, test_input))


    