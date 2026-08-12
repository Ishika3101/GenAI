import asyncio
import threading
import time

#we are running are application in asynchronous mode but also app has separate thread that just logs system health
def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️")

async def fetch_orders():
    await asyncio.sleep(3)  #time.sleep will not interfere this sleep
    print("🎁 order fetched")

#first get the thread ready
threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())