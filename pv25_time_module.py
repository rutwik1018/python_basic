#see hoe much time required to run code
#wait for result code run slowly slowly
import time

now_time=time.time()

for i in range(5):
    print("happy birthday ....!")
    time.sleep(2)

for j in range(5):
    print("happy diwali")
    time.sleep(2)

time_for_code=time.time()-now_time

print("time needed for code run ---> ",time_for_code)