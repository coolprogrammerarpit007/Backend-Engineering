# Asynchronous Python Programming


# Synchronous Programming

# Synchronous methods are Invoked, It completes executing before returning


import asyncio
import time


start = time.perf_counter()

async def task1():
    print("Send first Mail")
    asyncio.create_task(task2())
    await asyncio.sleep(5)
    print("First Email Reply!")
    
    
async def task2():
    print("Send Second Email")
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print("Second Email Reply")
    
    
async def task3():
    print("Sending Third Mail")
    await asyncio.sleep(2)
    print("Third Email Replied!")
    
    
asyncio.run(task1())

end = time.perf_counter()
print(f"Complete Time To Sent All The Mails: {end - start:.1f} Seconds")


# Asynchronous functions in python are typically called coroutines
# Coroutines decalred with the async/await syntax
# Coroutines are special functions that return coroutine objects when called