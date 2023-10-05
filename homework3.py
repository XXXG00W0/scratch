# homework3

def SelectionSort(array):
	for i in range(len(array)):
		minPos = i
		for j in range(i+1, len(array)):
			if array[minPos] > array[j]:
				minPos = j
		array[i], array[minPos] = array[minPos], array[i]
	return array
	 
print(SelectionSort([2,1,3,-5,7]))
print(SelectionSort([1,2,3,5,7]))
print(SelectionSort([9,7,5,3,1]))
