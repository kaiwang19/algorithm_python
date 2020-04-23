import sys


def merge(A, p, q, r):
    """
    Merge
    Introduction to Algorithms (3rd Chinese Edition), page 17.
    Authored by Kai Wang.
    2020-04-20
    :param A:unsorted list [p ... r]
    :param p:the lower bound of left list [p ... q]
    :param q:the upper bound of left list [p ... q]
    :param r:the upper bound of right list [q+1 ... r]
    :return:sorted list
    """
    L = A[p: q + 1]
    R = A[q + 1: r + 1]
    L.append(sys.maxsize)  # add an infinitely great value at the end to the list avoid index out of range
    R.append(sys.maxsize)  # add an infinitely great value at the end to the list avoid index out of range
    print("*** merge A="+str(A)+" when p,q,r= "+str(p)+","+str(q)+","+str(r)+" ***")
    print("*** left list L="+str(L)+" ***")
    print("*** right list R="+str(R)+" ***")

    i, j = 0, 0
    for k in range(p, r+1):
        print("*** merge k =" + str(k) + " ***")
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    print("*** after merge A="+str(A)+" when p,q,r= "+str(p)+","+str(q)+","+str(r)+" ***")


def merge_sort(A, p, r):
    """
    merge sort
    Introduction to Algorithms (3rd Chinese Edition), page 19.
    :param A: unsorted list [p ... r]
    :param p: the lower bound of unsorted list [p ... r]
    :param r: the upper bound of unsorted list [p ... r]
    :return:
    """
    print("*** merge_sort A="+str(A)+" when p,r= "+str(p)+","+str(r)+" ***")
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


# test
# TestList = [8, 2, 4, 9, 3, 6]
TestList = [5, 2, 4, 7, 1, 3, 2, 6]
merge_sort(TestList, 0, 7)
print("sorted result is "+str(TestList))
