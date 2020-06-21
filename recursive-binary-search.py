
import time

print("Recursive Binary Search")

t1 = 0
t2 = 0

steps = 0

# arg_arr = list(map(lambda x: x, range(100_000))) OR
arg_arr = [x for x in range(100_000)]

def search(arr, key):

	global t1
	global t2
	global steps

	t1 = time.time()
	arr.sort() # This step is neccessary for recursive binary search to work

	start_index = 0
	end_index = len(arr) - 1 
	mid_index = (start_index + end_index + 1) // 2 # using integer division here to avoid gettting a float which can cause an exception

	if key == arr[mid_index]:
		t2 = time.time()
		steps += 1
		return arr[mid_index]
	elif key < arr[mid_index]:
		t2 = time.time()
		steps += 1
		return search(arr[ : mid_index], key)
	elif key > arr[mid_index]:
		t2 = time.time()
		steps += 1
		return search(arr[mid_index - 1 : ], key)

result = search(arg_arr, 50_000)

print("found result: ", result, "after ", t2 - t1, "secs")
print("In", steps, "step(s)")