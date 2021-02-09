a = [1,2,3,0,0,1,0,2,0,1,0]

i = 0
j = i+1
while True:
    try:
        if a[i] == 0 and a[j] == 0:
            j+=1
        elif a[i] != 0 and a[j]== 0:
            i+=1
            j+=1
        elif a[i] != 0 and a[j] != 0:
            i+=1
            j+=1
        else:
            a[i], a[j] = a[j], a[i]
        print(i,j)
    except Exception as e:
        break

print(a)