def func(answered, needed, q):
    a = [i-j if i>=i else 0 for i,j in zip(needed, answered)]
    count = 0
    for k in sorted(a):
        if q >= k:
            count+=1
        else:
            break
        q-=k

    return count



if __name__ == '__main__':
    answered = [24, 27, 0]
    needed = [51, 52, 100]
    q = 100
    ans = func(answered, needed, q)
    print(ans)
