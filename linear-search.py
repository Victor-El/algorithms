"""
 This python script illustrates how to implement the linear search algorithm.
 The algorithm can also be easily implemented in any language of your choice
 The BigO notation for linear search is O(n)
"""
import time

print("Linear Search")

t1 = 0
t2 = 0

"""
The generation of this array takes a lot of time
When you run this program don't look at the time in 
your terminal or console, look at the time shown by
the program itself. Compare with the time of binary search.
You can increase or reduce the number of elements or change
you search number.
"""
arg_arr = list(map(lambda x: x, range(100_000_000)))

def search(arr, num):
	global t1
	global t2

	t1 = time.time()
	arr.sort()

	for i in arr:
		if i == num:
			t2 = time.time()
			return arr.index(i)

	t2 = time.time()
	return None

result = search(arg_arr, 5_000_000)

print("found result: ", result, "after ", t2 - t1, "secs")