"""
 This python script illustrates how to implement the recursive linear search algorithm.
 The algorithm can also be easily implemented in any language of your choice
 The BigO notation for time complexity of linear search is O(n)

 The major difference between linear search(iterative) and recursive is that
 linear search uses loops while it's recursive counterpart leaverages recursion.

 In most OOP and Imperative langusges, the space complexity recursive linear search
 will definitely impact the performance of the algoritms.

 Linear search and recursive linear search should have the same performance
 when implemented in a programming language that supports tail recursion.

 Overall linear search(iterative) has better performance than recursive unless
 the recursive algorithm is implementaed in a language that supports tail recousion.

 Languages that support tail recursion are functional programming languages such as
 Kotlin, Clojure, ReasonML, ..., etd.
"""

"""
Linear search algorithm works by comparing the search key with
every single element in a collection till it finds a match.
It is a simple algorithm but it is inefficient compared to
binary search.
"""

import time

print("Recursive Linear Search")

t1 = 0
t2 = 0
steps = 0

"""
The generation of this array takes a lot of time
When you run this program don't look at the time in 
your terminal or console, look at the time shown by
the program itself. Compare with the time of binary search.
You can increase or reduce the number of elements or change
you search number.
"""
arg_arr = list(map(lambda x: x, range(1_000)))

def search(arr, key):
	global t1
	global t2
	global steps

	start_index = 0
	arr.sort()

	if key != arr[start_index]:
		steps += 1
		t2 = time.time()
		return search(arr[start_index + 1:], key)
	elif key == arr[start_index]:
		steps += 1
		t2 = time.time()
		return arr[start_index]
	else:
		steps += 1
		t2 = time.time()
		return None

t1 = time.time()
result = search(arg_arr, 500)

print("found result: ", result, "after ", t2 - t1, "secs")
print("In", steps, "step(s)")