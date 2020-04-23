"""
heap
- build_max_heap : produce a max-heap from an unordered array
- max_heapify : correct a single violation of the heap property in a subtree at its root
- insert : insert element x into set S
- extract_max : return element of S with largest key and remove it from S
- heap_sort : return sorted list with heap
"""


def parent(i):
    return int(i+1/2)-1


def left(i):
    return 2*(i+1)-1


def right(i):
    return 2*(i+1)


def max_heapify(A, i):
    """
    max_heapify : correct a single violation of the heap property in a subtree at its root
    Introduction to Algorithms (3rd Chinese Edition), page 86.
    Authored by Kai Wang.
    2020-04-23
    :param A:unsorted list
    :param i:index of element that suppose to be the largest element
    :return:
    """
    left_index = left(i)
    right_index = right(i)
    print("max heapify with A = " + str(A) + " and i = " + str(i))
    # print("*** max heapify with left_index = " + str(left_index) + " ***")
    # print("*** max heapify with right_index = " + str(right_index) + " ***")
    largest_index = i  # suppose that A[i] is the largest value
    if left_index < len(A):
        if A[left_index] > A[i]:
            largest_index = left_index
    if right_index < len(A):
        if A[right_index] > A[largest_index]:
            largest_index = right_index
    if largest_index != i:
        largest_value = A[largest_index]
        A[largest_index] = A[i]
        A[i] = largest_value
        max_heapify(A, largest_index)


def build_max_heap(A):
    """
    build_max_heap : produce a max-heap from an unordered array
    there is no need to do anything with leaves at first, because leaves have no children
    then we build the tree from the bottom to the top
    Introduction to Algorithms (3rd Chinese Edition), page 87.
    Authored by Kai Wang.
    2020-04-23
    :param A: input list
    :return:
    """
    for i in range(int(len(A)/2)-1, -1, -1):
        max_heapify(A, i)


def heap_sort(A):
    """
    Introduction to Algorithms (3rd Chinese Edition), page 89.
    Authored by Kai Wang.
    2020-04-23
    :param A: unsorted list
    :return: sorted list
    """
    print("*** Input A = "+str(A)+" ***")
    build_max_heap(A)
    print("*** After building heaps, A = "+str(A)+" ***\n")
    result = []  # a list to save sorted list
    element_cnt = len(A)
    for i in range(element_cnt-1, 0, -1):
        # print("before swapping, A = " + str(A))
        result.append(A[0])  # save the largest number which is now the first element
        A[0] = A[-1]         # move the last element to the fist element
        A.pop()              # take away the last element
        max_heapify(A, 0)    # adjust the rest tree
        # print("->after heapify, A = " + str(A))
    result.append(A[0])      # save the rest element
    return result


# test
# TestList = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
TestList = [1, 3, 9, 8, 7, 10, 16, 2, 14, 4]
Res = heap_sort(TestList)
print("\n->sorted result is "+str(Res))
