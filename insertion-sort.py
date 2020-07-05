
def sort(arr):

	print(arr)

	for i in range(1, len(arr)):

		insert = arr[i]

		pos = i

		while pos > 0 and insert < arr[pos - 1]:
			arr[pos] = arr[pos - 1]
			pos -= 1


		arr[pos] = insert

	print("Sorted:", arr)


sort([2, 5,1,0,5,73,87,3,98,0,34,8])
