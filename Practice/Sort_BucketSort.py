# make assumptions that all values are within [lower_bound, upper_bound)
# the range is divided into bucket_cnt buckets
lower_bound = 0.0
upper_bound = 1.0
bucket_cnt = 10


def get_bucket_id(p):
    """
    calculate the bucket id of value p
    :param p: input value
    :return: bucket id
    """
    if (p < lower_bound) | (p >= upper_bound):
        return -1  # in case that value p is out of the assumed range
    else:
        bucket_size = (upper_bound - lower_bound) / bucket_cnt
        return int((p - lower_bound) / bucket_size)


def insertion_sort(A):
    """
    Insertion Sort
    Introduction to Algorithms (3rd Chinese Edition), page 14,
    Authored by Kai Wang.
    2020-04-19
    :param A: unsorted list
    :return: sorted list
    """
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def bucket_sort(A):
    """
    Bucket sort assumes that the input is drawn from a uniform distribution .
    It has an average-case running time of O(n).
    Introduction to Algorithms (3rd Chinese Edition), page 112.
    Authored by Kai Wang.
    2020-04-24
    :param A: unsorted list
    :return: sorted list
    """
    n = len(A)
    B = []
    for bucket_id in range(0, bucket_cnt):
        B.append([])  # initialize
    for i in range(0, n):
        bucket_id = get_bucket_id(A[i])  # add exception handling if A[i] is out of the assumed range
        B[bucket_id].append(A[i])
    for i in range(0, n):
        B[i] = insertion_sort(B[i])
    return B


# test
TestList = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
Res = bucket_sort(TestList)
print("\n->sorted result is "+str(Res))

# for i in Res:
#     for j in i:
#         print(j)
