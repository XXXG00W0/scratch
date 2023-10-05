# avl_heap
import math
import statistics as stats

class MedianHeap:

    def __init__(self):
        # A median heap consists of a min heap and a max heap
        self.min_heap = MinHeap()
        self.max_heap = MaxHeap()

    def median(self):
        # the median of the underlined non-empty array is:
	    # if both heaps have same size: 
        #   median is the mean of the top elements of the two heaps
        # else:
        #   median is the top elements of the heap with greater size
        if self.min_heap.heap_size() > self.max_heap.heap_size():
            return self.min_heap.top()
        elif self.min_heap.heap_size() < self.max_heap.heap_size():
            return self.max_heap.top()
        elif self.min_heap.heap_size() == self.max_heap.heap_size() and self.min_heap.heap_size() != 0:
            return (self.min_heap.top() + self.max_heap.top()) / 2.0
        else:
            return None

    def insert(self, key):
        # if the value of the element is less than the median:
        #   the new element is inserted to the max heap
        # if the value of the element is less than the median:
        #   the new element is inserted to the min heap
        # after each insertion, the size of the two heaps may differ by over 2
        # therefore, a balance action is required 
        median = self.median()
        if self.min_heap.top() == None:
            self.min_heap.min_heap_insert(key)
        elif key < median:
            self.max_heap.max_heap_insert(key)
        else:
            self.min_heap.min_heap_insert(key)
        self.heap_balance()
        
    def heap_balance(self):
        # putting one exccess element from the larger heap to the smaller heap 
        if self.min_heap.heap_size() > self.max_heap.heap_size() + 1:
            min_val = self.min_heap.extract_min()
            self.max_heap.max_heap_insert(min_val)
        elif self.max_heap.heap_size() > self.max_heap.heap_size() + 1:
            max_val = self.max_heap.extract_max()
            self.min_heap.min_heap_insert(max_val)


class Heap:

    def __init__(self) -> None:
        self.heap = []

    def heap_size(self) -> int:
        return len(self.heap)

    def left(self, i):
        return (i+1)*2-1

    def right(self, i):
        return (i+1)*2
    
    def parent(self, i):
        return (i+1)//2-1
    
    def top(self):
        if self.heap_size() > 0:
            return self.heap[0]
        else:
            return None 

class MinHeap(Heap):
    
    def heap_increase_key(self, i, key):
        if key > self.heap[i]:
            raise ValueError("new key is smaller than current key")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def min_heap_insert(self, key):
        self.heap.append(math.inf)
        i = self.heap_size()-1
        self.heap_increase_key(i, key)    
    
    def extract_min(self):
        if self.heap_size() == 0:
            return None
        min_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.min_heapify(0)
        return min_val
    
    def build_min_heap(self):
        for i in range(self.heap_size()//2-1, -1, -1):
            self.min_heapify(i)

    def min_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size() and self.heap[l] < self.heap[i]:
            smallest = l
        else:
            smallest = i
        if r < self.heap_size() and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

class MaxHeap(Heap):
    
    def heap_increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError("new key is smaller than current key")
        self.heap[i] = key
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def max_heap_insert(self, key):
        self.heap.append(-math.inf)
        i = self.heap_size()-1
        self.heap_increase_key(i, key)

    def extract_max(self):
        if self.heap_size() == 0:
            return None
        max_val = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop(-1)
        self.max_heapify(0)
        return max_val
    
    def build_max_heap(self):
        for i in range(self.heap_size()//2-1, -1, -1):
            self.max_heapify(i)

    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l < self.heap_size() and self.heap[l] > self.heap[i]:
            largest = l
        else:
            largest = i
        if r < self.heap_size() and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
        

    
mean_heap = MedianHeap()
arr = [2,4,1,3,5,7,3,6]
for i in arr:
    mean_heap.insert(i)
print(mean_heap.min_heap.heap)
print(mean_heap.max_heap.heap)
print(mean_heap.median())
print(stats.median(arr))

max_heap = MaxHeap()
arr1 = [3, 9, 5, 8, 15, 7, 4, 10, 6, 12, 16]
max_heap.heap = arr1
max_heap.build_max_heap()
# for i in arr1:
    # max_heap.max_heap_insert(i)
    # max_heap.build_max_heap()
print(max_heap.heap)
max_heap.extract_max()
print(max_heap.heap)
max_heap.max_heap_insert(11)
print(max_heap.heap)
