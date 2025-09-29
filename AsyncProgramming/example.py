import asyncio
import time
# await means in asynchronous programming is that we wait for the task to be complete, and once complete we return the result of the task to perform some action


async def t1():
    await t2()
    print("T1")

async def t2():
    await t3()
    print("T2")


async def t3():
    print("T3")


# asyncio.run(t1())

start = time.perf_counter()
async def file_reply():
    await asyncio.sleep(4)
    return "File Replied"

async def data_reply():
    await asyncio.sleep(2)
    return {"data",100}


async def task1():
    print("Waiting for the data.......")
    data = await data_reply()
    print(data)

async def task2():
    print("Waiting for the file.......")
    file = await file_reply()
    print(file)


async def main():
    x = asyncio.create_task(task1())
    y = asyncio.create_task(task2())

    await x 
    await y


# asyncio.run(main())
end = time.perf_counter()
# print(f"Complete time of Executing of Tasks: {end - start:.1f} Seconds")



# Code Challenge
# Create 3 coroutines named t1,t2, and t3. Each coroutine should print out the name of the coroutine. Call/run the first coroutine and using await have t2 print out first,
# t1 print out second and t3 print out first



async def t1():
    await t2()
    print("T1")

async def t2():
    print("T2")

async def t3():
    await t1()
    print("T3")


# asyncio.run(t3())


# Coding Challenge  2:- 

# Lets build a coroutine called fetch_data which simulates the collection of data from a network database. lets assume that takes a few seconds . It should return a dictionary {"data":100}. Next, build a new coroutine which counts down from 10 to 1 using range. using await, have each number print to the screen every 2 seconds. finally build a coroutine called main() and run fetch_data and the countdown coroutine concurrently. print the data that is returned from fetch_data whilst also counting down from 10


async def fetch_data():
    print("******** Fetching Data **********")
    await asyncio.sleep(5)
    print("*********** Data Returned ******")
    return {"data":100}


async def countdown():
    print("******** Counting down from 10 to 1")
    for i in range(10,1,-1):
        print(i)
        await asyncio.sleep(2)
    print("Countdown Completed")

async def main():
    x = asyncio.create_task(fetch_data())
    y = asyncio.create_task(countdown())
    await x
    print(x)
    await y

asyncio.run(main())

