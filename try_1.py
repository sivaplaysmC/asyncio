import asyncio

async def foo() :
    while True : 
        print("Hi" , end=" ")
        await asyncio.sleep(0)
async def main() :
    print("Started")
    _ = asyncio.create_task(foo())
    await asyncio.sleep(2)
    print("Ended")

asyncio.run(main())
