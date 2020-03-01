import time
l1 = list(range(1,10000))

start_time = time.time()
print(max(list(filter(lambda x:x<max(l1), l1))))
end_time = time.time()

print("Time required is:{}".format(end_time - start_time))



#############################################################


start_time1 = time.time()
highest = l1[0]
second = 0

for i in range(1,len(l1)):
    if l1[i] > highest:
        second = highest
        highest = l1[i]

print(second)

end_time1 = time.time()
print("Time required is:{}".format(end_time1 - start_time1))







/*
OUTPUT

pradip@PradipK-LT:~/Practice$ python sample.py 
9998
Time required is:1.2643871307373047
9998
Time required is:0.001409769058227539
pradip@PradipK-LT:~/Practice$ 


*/
