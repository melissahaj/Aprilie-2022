import time

# help si dir

start = time.time()

for i in range(1000):
    print(10 ** i)

stop = time.time()

print("Start at:", start)
print("End at:", stop)
print("Duration:", stop - start)
