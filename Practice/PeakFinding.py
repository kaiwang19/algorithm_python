"""
Based on MIT 6.006 Lec01 - Algorithmic thinking, peak finding
Q1 - 1D peak finding
Q2 - 2D peak finding
"""

import time

"""
Q1 - [One-dimensional Version]
Position 2 is a peak if and only if b ≥ a and b ≥ c. Position 9 is a peak if i ≥ h.
+ 1 2 3 4 5 6 7 8 9  
+ a b c d e f g h i  
Problem: Find a peak if it exists (Does it always exist?)
Tips: You just have to find the first peak, which means there is no need to find all peaks.
"""


# Sol -> Brute Force
# return position
def peakfinding_1d_bf(data):
    n = len(data)
    position = -1  # default value is -1, which is obviously not a valid index of the input list
    if n < 3:
        return position  # too small list
    elif data[0] > data[1]:  # the definition of 'peak' is not so accurate, this case might be possible
        position = 0
        return position
    else:
        for i in range(1, n - 2):
            if data[i - 1] <= data[i] & data[i] >= data[i + 1]:
                position = i
                return position
        if data[n - 2] <= data[n - 1]:
            position = n - 1
        return position


# Sol -> Divide and Conquer
# return value
def peakfinding_1d_dc(data):
    print(data)
    n = len(data)
    if n == 1:
        return data[0]
    elif n == 2:
        if data[0] >= data[1]:
            return data[0]
        else:
            return data[1]
    else:
        middle = int(n/2)
        print('middle value is list[' + str(middle) + ']:' + str(data[middle]))
        if data[middle-1] > data[middle]:
            print("select left")
            return peakfinding_1d_dc(data[0:middle])  # exclude data[middle]
        elif data[middle+1] > data[middle]:
            print("select right")
            return peakfinding_1d_dc(data[middle+1:])
        else:
            print("select middle")
            return data[middle]


# Test Data
# TestList = [6, 5, 4, 3, 2, 1, 4, 3]
TestList = [6, 7, 4, 3, 2, 1, 4, 5]

# Test 1D-PeakFinding-BruteForce
print("==== 1D-PeakFinding-BruteForce starts ====")
start = time.process_time_ns()
PeakIndexBF = peakfinding_1d_bf(TestList)
end = time.process_time_ns()
print("==== 1D-PeakFinding-BruteForce ends with execution time:", end - start, "ns. ====")
print("Peak index is TestList[" + str(PeakIndexBF) + "] : " + str(TestList[PeakIndexBF]))

# Test 1D-PeakFinding-Divide&Conquer
print("==== 1D-PeakFinding-Divide&Conquer starts ====")
start = time.process_time_ns()
PeakValueDC = peakfinding_1d_dc(TestList)
end = time.process_time_ns()
print("==== 1D-PeakFinding-Divide&Conquer ends with execution time:", end - start, "ns. ====")
print("Peak value is " + str(PeakValueDC))
