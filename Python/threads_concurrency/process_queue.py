from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready") #method doesn't just return the value it puts the value in queue



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())