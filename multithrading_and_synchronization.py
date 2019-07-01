import threading
x = 0

def increment():
    global x
    x+=1

def start_thread(lock):
    for _ in range(1000000):
        lock.acquire()
        increment()
        lock.release()

def main_thread():

    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=start_thread, args=(lock,))
    t2 = threading.Thread(target=start_thread, args=(lock,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == '__main__':
    for i in range(10):
        main_thread()
        print("Thread cycle:{0} and it's value is={1}".format(i,x))
