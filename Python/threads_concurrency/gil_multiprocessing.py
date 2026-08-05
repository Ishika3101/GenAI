from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__": #without this line it can give runtime error as process doesnt have all info so basically it doesnt get to know entrypoint of the program
    start = time.time()

    p1 = Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds")
