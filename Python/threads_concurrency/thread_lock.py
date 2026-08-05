import threading

counter=0
lock=threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:  #it locks that particular memory location
            counter+=1 
#we have created thread safe method

threads=[threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")