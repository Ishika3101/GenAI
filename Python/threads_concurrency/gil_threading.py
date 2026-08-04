import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...") #.name gives name of the thread
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...")

thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

#it will start the time
start = time.time() #time.time() is a function from Python's time module that returns the current time as the number of seconds since the Unix Epoch. The most common use is measuring how long a program takes to run.
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds")