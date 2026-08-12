import asyncio

async def brew(name):
    print(f"brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready")

async def main():  #main can also be coroutine
    await asyncio.gather(brew("masala chai"),
                         brew("ginger chai"),
                         brew('green chai')
                         )

asyncio.run(main())  #here we will wait combined 2 seconds as it is non blocking operation others continue their work and all 3 chai will come together

