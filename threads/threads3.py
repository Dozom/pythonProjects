from threading import Thread
import time

def thread1():
    print("Thread 1 started")
    time.sleep(10)
    print("Thread 1 ended")

def thread2():
    print("Thread 2 started")
    time.sleep(4)
    print("Thread 2 ended")

print("Main start")
t1 = Thread(target=thread1)
t2 = Thread(target=thread2)
t1.start()
t2.start()
#t1.join()
#t2.join()
print("Main end")
