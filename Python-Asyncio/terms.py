# asyncio is a python built-in library to write concurrent code using the async/await syntax enabling efficient handling of I/O bound operations by switching b/w tasks not by blocking them
#It operates on an event loop within a single thread, allowing multiple coroutines to run concurrently, making it ideal for high-performance network servers, web frameworks, and other I/O-heavy applications.  

# Event Loop is the engine which runs the asynchronous functions. It's kind of scheduler which keeps track of all our tasks and if a task is suspended it takes control back to event loop to start or resume a new task
import asyncio
import time


def sync_function(test_param:str) -> str:
    print("This is a synchronous function")
    time.sleep(2)
    return f"Sync Result: {test_param}"

async def main():
    # sync_result = sync_function("Test")
    # print(sync_result)
    pass





if __name__ == "__main__":
    asyncio.run(main())