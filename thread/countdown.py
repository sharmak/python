import time
import threading
class CountDownThread(threading.Thread):
    def __init__(self, count):
        threading.Thread.__init__(self)
        self.count = count
    def run(self):
        while self.count > 0:
            print "Count Down %s " %str(self.count)
            self.count -= 1
            time.sleep(1)
if __name__ == '__main__':
    t1 = CountDownThread(5)
    t1.start()
    
            

