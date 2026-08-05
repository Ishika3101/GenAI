from multiprocessing import Process,Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value+=1

if __name__=="__main__":
    counter=Value('i',0) #key value pair
    processes=[Process(target=increment,args=(counter,)) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value:",counter.value)

#now each process is able to share the value

#Processes in Python have separate memory spaces, so they cannot directly access each other's variables. multiprocessing.Value is used to create a shared variable that multiple processes can read and modify. multiprocessing.Queue is used for inter-process communication (IPC), allowing one process to safely send data or results to another. Value is suitable for sharing simple data, while Queue is suitable for passing messages or larger objects between processes.
