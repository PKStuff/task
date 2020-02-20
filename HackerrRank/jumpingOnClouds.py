def jumpingOnClouds(c):
    n = len(c)
    i = 0
    count = 0
    while i < n:
        if (i+2) < n and c[i+2] == 0:
            i+=2
            count+=1
        elif (i+1) < n and c[i+1] == 0:
            i+=1
            count+=1
        else:
            break
    return count



c = [0, 0, 1, 0, 0, 1, 0]
ans = jumpingOnClouds(c)
print(ans)
