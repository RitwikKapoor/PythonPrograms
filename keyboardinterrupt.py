import time
import signal

def my_handler(signal,frame):
    print("I am interrupt")

signal.signal(signal.SIGINT, my_handler)

num = 0
while True:
    num += 1
    print("Hello", num)
    time.sleep(1)


# kill -9 $(ps aux | grep "python3 keyboardinterrupt.py" | grep -v color | tr -s ' ' | cut -d ' ' -f 2)
# kill -9 $(ps aux | grep "python3 keyboardinterrupt.py" | grep -v color | awk '{print $2}')

