#only single core is performing the task and threads switches
import threading
import time

def order_chai():
    for i in range(1,4):
        print(f"ordering order for {i}")
        time.sleep(1)

def brew_chai():
    for i in range(1,4):
        print(f"brewing order for {i}")
        time.sleep(2)

#create threads
order_thread=threading.Thread(target=order_chai)
brew_thread=threading.Thread(target=brew_chai)

#invoke
order_thread.start()
brew_thread.start()

#wait for both to finish
order_thread.join()
brew_thread.join()

print(f"all orders taken and brewed")

#without thread
# Main Thread
# │
# ├── Start order thread
# ├── Start brew thread
# └── Immediately print "All orders taken and brewed"

# Order Thread
# │
# ├── Taking order 1
# ├── Taking order 2
# └── ...

# Brew Thread
# │
# ├── Brewing order 1
# ├── Brewing order 2
# └── ...

#with join
# Main Thread
# │
# ├── Start order thread
# ├── Start brew thread
# ├── Wait (join)
# │
# │   Order thread finishes
# │   Brew thread finishes
# │
# └── Print "All orders taken and brewed"