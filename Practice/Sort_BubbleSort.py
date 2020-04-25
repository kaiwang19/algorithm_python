def bubble_sort(A):
    """
    bubble sort - popular but quite slow
    Introduction to Algorithms (3rd Chinese Edition), page 23.
    Authored by Kai Wang.
    2020-04-24
    :param A: unsorted list
    :return: sorted list
    """
    for i in range(0, len(A)-1):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j-1]:
                A[j], A[j-1] = A[j-1], A[j]


# test
TestList = [1, 3, 9, 8, 7, 10, 16, 2, 14, 4]
bubble_sort(TestList)
print("\n->sorted result is "+str(TestList))
