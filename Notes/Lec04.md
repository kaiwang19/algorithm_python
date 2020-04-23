4	Heaps and heap sort  
===

Check slides here:   
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec04.pdf  

check videos here:  
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/lecture-4-heaps-and-heap-sort/  

---

## Priority Queues  
Priority Queue  
A data structure implementing a set S of elements, each associated with a key, supporting the following operations:  
+ insert(S, x)          :insert element x into set S
+ max(S)                :return element of S with largest key
+ extract_max(S)        :return element of S with largest key and remove it from S
+ increase_key(S, x, k) :increase the value of element x’ s key to new value k (assumed to be as large as current value)  

## Heaps  
Heaps  
+ Implementation of a priority queue (* *Todo: Other Implementations & Comparing Stacks queue and priority queue* *)
+ An **array**, visualized as a **nearly complete binary tree**
+ Max Heap Property: The key of a node is ≥ than the keys of its children (Min Heap defined analogously)  

\*Heap Operations\*  
- build_max_heap : produce a max-heap from an unordered array  
- max_heapify : correct a **single** violation of the heap property in a subtree at its root
- insert
- extract_max
- heap_sort

## Heap Sort  
Heap Sort Strategy:  
1. Build Max Heap from unordered array;  
2. Find maximum element A[1];  
3. Swap elements A[n] and A[1]: now max element is at the end of the array!  
4. Discard node n from heap (by decrementing heap-size variable)  
5. New root may violate max heap property, but its children are max heaps. Run max_heapify to fix this.  
6. Go to Step 2 unless heap is empty  

Heap Sort Complexity - O(n log n)  
- after n iterations the Heap is empty  
- every iteration involves a swap and a max_heapify operation; hence it takes O(log n) time  
