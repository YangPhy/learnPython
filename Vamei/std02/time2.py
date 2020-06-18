import time
print('start')
print(time.perf_counter())
print(time.process_time())
time.sleep(10)
print('wake up')
print(time.perf_counter())
print(time.process_time())

