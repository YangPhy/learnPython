import signal
import time
# Define signal handler function
def myHandler(signum,frame):
    print("Now, it is the time")
    exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)
signal.alarm(3)
while True:
    time.sleep(1)
    print('not yet')
