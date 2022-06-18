import time

some_ts = 136182479728939.354643

ts_struct = time.gmtime(some_ts)
print(ts_struct.tm_hour)
print(ts_struct.tm_min)
