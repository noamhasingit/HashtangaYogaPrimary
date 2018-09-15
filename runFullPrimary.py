import yoga
import threading
import time

exitFlag = 0


class myThread (threading.Thread):


    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self._event = threading.Event()
        self.threadID = threadID
        self.name = name
        self.counter = counter
        print(self._event)

    def run(self):
        print("Starting " + self.name)
        while True:
            print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)

    def pause(self):
        print(self.name,"Pause")
        self._event.clear()

    def resume(self):
        self._event.set()

    def _wait_if_paused(self):
        self._event.wait()


def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

# Create new threads
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

thread1.pause()
thread1._wait_if_paused()
thread1.join()
print ("Exiting Main Thread")