def pushZerosToEnd(arr, n):
	counter = 0
	for index,element in enumerate(arr):
		if element == 0:
			counter += 1
			arr.append(0)

	for value in range(counter - 1):
		arr.remove(0)

	return arr

def main():
	print(pushZerosToEnd([3,5,0,0,4],5))

main()
