def balancedSums(arr):
    left_sum = sum(arr)
    total_sum = 0
    flag = False
    for i in arr:
        left_sum -= i
        if total_sum == left_sum:
            flag = True
            break
        total_sum+=i
    if flag:
        return "YES"
    return "NO"
