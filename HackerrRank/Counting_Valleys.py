def countingValleys(n, s):
    count = 0
    sum1 = 0
    for i in s:
        if i == 'D':
            sum1-=1
        elif i == 'U':
            tmp = sum1
            sum1+=1
            if tmp < 0 and sum1==0:
                count+=1
                sum1 = 0
    return count



n = 12
s = 'UDDDUDUU'
ans = countingValleys(n, s)
print(ans)
