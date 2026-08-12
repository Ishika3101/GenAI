import asyncio

async def brew():  #async keyword declares a coroutine
    print("brewing...")
    await asyncio.sleep(2) #await keyword here is the non blocking way to simulate awaiting. it doesnt block the main thread
    print("done")

asyncio.run(brew())