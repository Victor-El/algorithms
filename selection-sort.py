"""
 Selection sort is a sorting algorithm that has a time complexity BigO notation of O(n^2).
 Selection sorts with two loops: The Outer loop is responsible for selecting one item while the 
 inner loop is responsible for doing the comparison and swapping of values.
"""

# def sort(arr):
# 	for i in range(len(arr)):
# 		for j in range(len(arr)):
# 			if arr[i] < arr[j]:
# 				arr[i], arr[j] = arr[j], arr[i]

# 	print(arr)

def sort(arr):
	print(arr)

	for i in range(len(arr)):
		min = i

		for j in range(i + 1, len(arr)):
			if arr[min] > arr[j]:
				min = j

		arr[i], arr[min] = arr[min], arr[i]

	print("Sorted: ", arr)

sort([2, 5,1,0,5,73,87,3,98,0,34,8])
