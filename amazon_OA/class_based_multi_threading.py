import threading 
import time
class worker(threading.Thread):
    def run(self):
        for i in xrange(10):
            print self.getName,i
            time.sleep(0.1)


t1 = worker()
t2 = worker()

t1.start()
t2.start()
