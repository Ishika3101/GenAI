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

#why we write if name==maim
# because It prevents child processes from re-running the entire script when they are created.
# Without if __name__ == "__main__"
# Main Process
#       │
#       ▼
# Creates Child
#       │
#       ▼
# Child executes whole file
#       │
#       ▼
# Creates another Child
#       │
#       ▼
# Creates another Child
#       │
#       ▼
# Infinite process creation ❌
# With if __name__ == "__main__"
# Main Process
#       │
#       ▼
# Creates Child
#       │
#       ▼
# Child imports file
#       │
#       ▼
# Skips the if block
#       │
#       ▼
# Runs only task() ✅
