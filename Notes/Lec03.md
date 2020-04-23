3	Insertion sort, merge sort  
===

Check slides here:   
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec03.pdf  

check videos here:  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-3-insertion-sort-merge-sort/  

---

## Insertion Sort  
Insertion Sort Complexity - Θ(n2)   
+ Θ(n2) compares  
+ Θ(n2) swaps  

Binary Insertion Sort Complexity - Θ(n2)   
Binary search only take Θ(log n) time. However, shifting the elements after insertion will still take Θ(n) time.   
+ Θ(n log n) compares  
+ Θ(n2) swaps  

## Merge Sort  
Merge Sort Complexity - Θ(n lg n)  
- Divide and Conquer  
- Merging two sorted arrays: Time = Θ(n) to merge a total of n elements (linear time).  
T(n) = Θ(1), if n = 1;  
T(n) = 2T(n/2) + Θ(n), if n > 1  
Total Complexity = Θ(n lg n)  
Equal amount of work done at each level.  

## Other Recursion Models Complexity  
T(n) = 2T(n/2) + c, where c > 0 is constant.   
Total Complexity = Θ(n)  
All the work done at the leaves.  

T(n) = 2T(n/2) + cn2, c > 0 is constant.  
Total Complexity = Θ(n2)  
All the work done at the root.  
