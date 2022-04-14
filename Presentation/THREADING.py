import threading
import time

def sleepy_man():
    print('Starting to sleep inside')
    time.sleep (1)
    print('Woke up inside')
x = threading.Thread(target = sleepy_man)
x.start()
print (threading.activeCount())
time.sleep(1.2)

print('Done')