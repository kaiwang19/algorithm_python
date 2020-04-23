
def insertion_sort(A):
    """
    Insertion Sort
    Introduction to Algorithms (3rd Chinese Edition), page 14,
    Authored by Kai Wang.
    2020-04-19
    :param A: unsorted list
    :return: sortted list
    """
    for j in range(len(A)):
        # print("j equals " + str(j) + " when dealing with list " + str(A))
        key = A[j]
        # insert A[j] into sorted sequence A[0..j-1]
        i = j - 1
        while i > -1 and A[i] > key:
            # print("switch at A[" + str(i) + "]: " + str(A[i]) + " while key is " + str(key))
            A[i + 1] = A[i]
            i = i - 1
            # print("after switching half, the list is " + str(A))  # always put larger numbers first
        A[i + 1] = key
    return A


# test
# TestList = [6, 7, 4, 3, 2, 1, 4, 5]
TestList = [8, 2, 4, 9, 3, 6]
Res = insertion_sort(TestList)
print("sorted result is "+str(Res))
