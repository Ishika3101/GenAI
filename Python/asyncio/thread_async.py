import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"checking {item} in store")
    time.sleep(3)  #blocking operation
    return f"{item} stock:42"

async def main():
    loop=asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result=await loop.run_in_executor(pool,check_stock,"masala tea")
        print(result)

asyncio.run(main())

        #          Event Loop
        #              │
        #              │
        #              ▼
        #       run_in_executor()
        #              │
        #              ▼
        #         Thread Pool
        #              │
        #              ▼
        #       Worker Thread
        #              │
        #              ▼
        #   check_stock("masala tea")

#run_in_executor() allows an async event loop to execute a blocking synchronous function in a separate thread or process without blocking the event loop. await pauses the current coroutine until that executor task completes while allowing the event loop to handle other tasks.