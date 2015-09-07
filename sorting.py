"""
@author mbartoli

Sorting.py -- a compilation of various sorting algorithms 

Sorting algorithms currently included: 
- Insertation Sort

"""



def insertation_sort(unsorted):
	""" 
	Insertation sort -- O(n^2) 

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

	"""
	for j in range(1,len(unsorted)-1):
		key = unsorted[j]
		i = j
		while i > 0 and unsorted[i-1] > key:
			unsorted[i] = unsorted[i-1]
			i = i-1
		unsorted[i] = key
	return unsorted


def main():
	unsorted = [24,4,5,29,29,39,17,10,11,20,32]
	sorted = [4,5,10,11,17,20,24,29,29,39,32]
	assert insertation_sort(unsorted) == sorted


if __name__ == '__main__':
	main()