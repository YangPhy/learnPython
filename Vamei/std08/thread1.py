# A program to simulate selling tickets in multi-thread way

import threading
import time
import os

# This function could be any function to do other chores
def doChore():
    time.sleep(0.5)

# Function for each thread
def booth(tid):
    global i
    global lock
    while True:
        lock.acquire()                 # Lock; or wait if other thread is holding the lock
        if i!=0:
            i=i-1                      # Sell tickets
            print(tid,': now left:',i) # Tickets left
            doChore()                  # Other critical operations
        else:
            print("Thread_id",tid,"No more tickerts")
            os._exit(0)                # Exit thie whole process
            immediatedly
        lock.release()                 # Unblock
        doChore()                      # Non-critical operations

# Start of the main function
i = 100                                # Available ticket number
lock= threading.Lock()                 # Lock (i.e., mutex)

# Start 10 threads
for k in range(10):
    new_thread= threading.Thread(target=booth,args=(k,))
    new_thread.start()
