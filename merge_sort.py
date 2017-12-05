from random import randint
from random import random
from time import time

def merge_sort(arr):
	# recursively divide arrays into 2 halfs and merge
	if len(arr)<=1:
		return arr

	middle = len(arr)/2
	left = arr[0:middle]
	right = arr[middle:]
	left = merge_sort(left)
	right = merge_sort(right)
	
	return merge_halfs(left,right)

def merge_halfs(left, right):
	# take 2 arrays and merge them
    result = []
       
    while(left and right):
    	if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    return result + left if left else result + right

def test_merge_sort():
	# test 1: array length 2**n for n in [0:10]
	length = [2**n for n in range(10)]
	for l in length:
		num = l
		arr = [randint(-100,100) for i in range(num)]
		assert sorted(arr) == merge_sort(arr)
	print ("test 1 - int values[-100;100], array length 2**n for n in [0,10] - pass")
	# test 2: float values in array
	num = 2**10
	arr = [random()*200 - 100 for i in range(num)]
	assert sorted(arr) == merge_sort(arr)
	print ("test 2 - float values [-100;100], arr length 2**10 - pass")
	# test 3: characters in array
	arr = ["zc", 103, "a", "c", "b", "e"]
	assert sorted(arr) == merge_sort(arr)
	print ("test 3 - array of characters - pass")

def time_merge_sort():
	length = [2**n for n in range(0,10)]
	for l in length:
		num = l
		arr = [randint(-100,100) for i in range(num)]
		t0 = time()
		merge = merge_sort(arr)
		t1 = time()
		print num, t1-t0

def main():
	test_merge_sort()
	time_merge_sort()

if __name__ == '__main__':
    main()