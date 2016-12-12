import time
import thread
import threading
def thread_function(name, n, delay):

    for i in xrange(n):
        threadLock.acquire()
        print name, i
        threadLock.release()
        time.sleep(delay)

try:
    thread.start_new_thread(thread_function, ("T-1",100,1))
    thread.start_new_thread(thread_function, ("T-2",100,1.5))
except:
    print "ERROR"

threadLock = threading.Lock()

while 1:
    pass