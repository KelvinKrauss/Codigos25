import time

start = time.time()

n=[50,40]

for x in n:
    for i in range(x):
         print("0")  
         print("1")


end = time.time()
print(":", end - start, "segundos")
