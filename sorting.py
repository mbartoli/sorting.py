"""
@author mbartoli

Sorting.py -- a compilation of various sorting algorithms 

Sorting algorithms currently included: 
- Insertation Sort
- Merge Sort

"""



def insertation_sort(unsorted):
	""" 
	Insertation sort -- Worst: O(n^2), Best: O(n), Average: O(n^2)

	Insertion sort iterates, consuming one input element each repetition,
	and growing a sorted output list. Each iteration, insertion sort
	removes one element from the input data, finds the location it belongs
	within the sorted list, and inserts it there. It repeats until no input
	elements remain.

	Sorting is typically done in-place, by iterating up the array, growing
	the sorted list behind it. At each array-position, it checks the value 
	there against the largest value in the sorted list (which happens to be
	next to it, in the previous array-position checked). If larger, it
	leaves the element in place and moves to the next. If smaller, it finds
	the correct position within the sorted list, shifts all the larger
	values up to make a space, and inserts into that correct position.

	Other things to know: 
	- Efficient for (quite) small data sets
	- More efficient in practice than most other simple quadratic. 
	  (i.e., O(n2)) algorithms such as selection sort or bubble sort and 
	  usually faster in practice than asymptotically faster algorithms for
	  small data sets.
	- Adaptive, i.e., efficient for data sets that are already 
	  substantially sorted: the time complexity is O(nk) when each element 
	  in the input is no more than k places away from its sorted position.
	- Stable; i.e., does not change the relative order of elements with 
	  equal keys.
	- In-place; i.e., only requires a constant amount O(1) of additional
	  memory space.
	- Online; i.e., can sort a list as it receives it.
	"""
	for j in range(1,len(unsorted)):
		key = unsorted[j]
		i = j
		while i > 0 and unsorted[i-1] > key:
			unsorted[i] = unsorted[i-1]
			i = i-1
		unsorted[i] = key
	return unsorted


def merge_sort(unsorted):
	"""
	Merge sort -- Worst: O(n log n), Best: O(n log n), Average: O(n log n)

	Conceptually, a merge sort works as follows:
    	1) Divide the unsorted list into n sublists, each containing 1 element 
	   (a list of 1 element is considered sorted).
   	2) Repeatedly merge sublists to produce new sorted sublists until there
	   is only 1 sublist remaining. This will be the sorted list.
	   
	Other things to know:
	- Achieves O(n) when the input is already sorted
	"""	
	if len(unsorted) == 1:
		return unsorted
	middle = len(unsorted)/2
	left, right = unsorted[:middle], unsorted[middle:]
	left, right = merge_sort(left), merge_sort(right)
	return merge(left,right)

def merge(left,right):
	""" 
	Auxillary function for merge sort 
	"""
	result = [] 
	l_idx, r_idx = 0, 0
	while l_idx < len(left) and r_idx < len(right):
		if left[l_idx] <= right[r_idx]:
			result.append(left[l_idx])
			l_idx += 1
		else:
			result.append(right[r_idx])
			r_idx += 1
	if left:
		result.extend(left[l_idx:])
	if right:
		result.extend(right[r_idx:])
	return result 



def main():
	unsorted = [24,4,5,29,29,39,17,10,11,20,32]
	sorted = [4,5,10,11,17,20,24,29,29,32,39]
	assert insertation_sort(unsorted) == sorted
	assert merge_sort(unsorted) == sorted


if __name__ == '__main__':
	main()
