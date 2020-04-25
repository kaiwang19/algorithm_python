def partition(A, p, r):
    """
    Try to divide the list into 2 lists with a pivot element(let it be A[r] here)
    After partition, elements in left list <= pivot element while elements in right list > pivot element
    Authored by Kai Wang.
    2020-04-25
    :param A: unsorted list [p ... r]
    :param p: the lower bound of unsorted list [p ... r]
    :param r: the upper bound of unsorted list [p ... r]
    :return: indexed position of pivot element
    """
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(A, p, r):
    """
    Introduction to Algorithms (3rd Chinese Edition), page 95.
    Similar to merge sort, the algorithm adopts divide-and-conquer strategy
    Complexity:  O(n log n)
    Authored by Kai Wang.
    2020-04-25
    :param A: unsorted list [p ... r]
    :param p: the lower bound of unsorted list [p ... r]
    :param r: the upper bound of unsorted list [p ... r]
    :return:
    """
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)


# test
TestList = [5, 2, 4, 7, 1, 3, 2, 6]
quick_sort(TestList, 0, 7)
print("sorted result is "+str(TestList))
