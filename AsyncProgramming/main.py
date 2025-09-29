print("************ Asynchronous Programming *************")


# Synchronous methods are invoked, it completes executing before returning


# Synchronous Way

import time
import asyncio



# start = time.perf_counter()
# def task1():
#     print("Sending first mail")
#     print("Waiting for first Person to reply")
#     time.sleep(5)
#     print("First Person Replied")
#     task2()


# def task2():
#     print("Sending Second Mail")
#     print("Waiting for second person to reply")
#     time.sleep(3)
#     print("Second Person Replied")
#     task3()


# def task3():
#     print("Sending Mail to the third Person")
#     print("Waiting for the third person to reply")
#     time.sleep(2)
#     print("Third Person Replied")


# # task1()

# end = time.perf_counter()
# print(f"Complete time of Executing of Tasks: {end - start:.1f} Seconds")


# Transforming Above code to Asynchronous

start = time.perf_counter()
async def task1():
    print("Sending Mail to the first Person..")
    print("Waiting for the first person to reply..")
    asyncio.create_task(task2())
    await asyncio.sleep(5) # simulating that mail takes 5 second to reply
    print("First Person Replied to the mail successfully...")


async def task2():
    print("Sending Mail to the Second Person..")
    print("Waiting for the Second person to reply..")
    asyncio.create_task(task3())
    await asyncio.sleep(3)
    print("Second Person Replied to the mail successfully...")

async def task3():
    print("Sending Mail to the third Person..")
    print("Waiting for the third person to reply..")
    await asyncio.sleep(2)
    print("Third Person Replied to the mail successfully...")



asyncio.run(task1())
end = time.perf_counter()
print(f"Complete time of Executing of Tasks: {end - start:.1f} Seconds")