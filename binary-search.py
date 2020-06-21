"""
 This python script illustrates how to implement the binary search algorithm.
 The algorithm can also be easily implemented in any language of your choice
"""

"""
Binary search works by first sorting an array,
finding the middle element and then checking if the middle element
is equal to the search element, if true then it return that element
else it checks if the search key is greater than the middle element,
if true, it splits the array into two, it focuses on the sublist or 
sub array of the main list or array that is lower than the initial mid
element. The algorithm keeps iterating this process till it finds a match.
The BigO notation of binary search id O(log n)
"""

import time

print("Binary Search")

t1 = 0
t2 = 0

steps = 0

"""
The generation of this array takes a lot of time
When you run this program don't look at the time in 
your terminal or console, look at the time shown by
the program itself. Compare with the time of linear search.
You can increase or reduce the number of elements or change
you search number.
"""
arg_arr = list(map(lambda x: x, range(1_000_000)))

t1 = 0
t2 = 0
steps = 0

def search(arr, key):
	global t1
	global t2
	global steps

	t1 = time.time()
	arr.sort() # This step is neccessary for binary search to work

	start_index = 0
	end_index = len(arr) - 1 
	mid_index = (start_index + end_index + 1) // 2 # using integer division here to avoid gettting a float which can cause an exception
	element = None

	if key > arr[end_index]:
		t2 = time.time()
		return element


	while element == None and end_index <= end_index:
		steps += 1

		if key == arr[mid_index]:
			element = arr[mid_index]
		if key > arr[mid_index]:
			start_index = mid_index + 1
			mid_index = (start_index + end_index + 1) // 2
		if key < arr[mid_index]:
			end_index = mid_index - 1
			mid_index = (start_index + end_index + 1) // 2

	t2 = time.time()
	return element

	

result = search(arg_arr, 1_000_000)

print("found result: ", result, "after ", t2 - t1, "secs")
print("In", steps, "steps")