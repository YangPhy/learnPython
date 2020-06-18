import time
print(time.time())
# DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
# print(time.clock())
print(time.process_time())
print(time.perf_counter())
