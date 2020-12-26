def equillium(arr, n):
	left_sum, right_sum = 0, sum(arr)
	for i in range(0, n):
		right_sum -= arr[i]
		if right_sum == left_sum:
			return i
		left_sum += arr[i]
	return -1

arr = [-7, 1, 5, 2, -4, 3, 0]

print(equillium(arr, len(arr)))
