# asyncio python
# asyncio is Python's built-in library for writing concurrent code using the async/await syntax. This approach is ideal for I/O-bound tasks—operations that involve waiting for external resources, such as network requests, database queries, or file access. 
# Instead of blocking the entire program while waiting, asyncio allows multiple tasks to run in a single thread by taking turns. When one task needs to wait, it voluntarily gives up control, letting the program execute other tasks in the meantime. 
# Key concepts
# Coroutines: These are special functions defined with async def. A coroutine can be paused during execution by an await call and resumed later.
# async and await:
# The async keyword is used to define an asynchronous function (a coroutine).
# The await keyword is used inside an async function to pause its execution until the awaited task is complete. It tells the program to "wait for this to finish, but do other work in the meantime".
# Event Loop: The central component of asyncio that manages and schedules the execution of coroutines. It keeps track of all the tasks and switches between them whenever an await call yields control.
# Tasks: A task is an asyncio object that wraps a coroutine and schedules it to run on the event loop. You create a task with asyncio.create_task() or run multiple tasks with asyncio.gather(). 
# Example: Sync vs. Async requests
# This example compares a synchronous approach to a concurrent asyncio approach for fetching data from multiple URLs. 
# Synchronous approach
# The program waits for each request to complete before starting the next, leading to a total runtime that is the sum of all wait times. 
# python

import time
import requests_file

def fetch_sync(url):
    print(f"Fetching {url}...")
    response = requests_file.get(url)
    print(f"Done fetching {url} with status code {response.status_code}.")

def main_sync():
    start = time.perf_counter()
    urls = ['https://httpbin.org/delay/1', 'https://httpbin.org/delay/2']
    for url in urls:
        fetch_sync(url)
    end = time.perf_counter()
    print(f"Synchronous execution time: {end - start:.2f} seconds")

if __name__ == "__main__":
    main_sync()

# Expected output: ~3.00 seconds (1s + 2s)

# Asynchronous approach
# By using asyncio with an asynchronous library like aiohttp, the program can send multiple requests and wait for all of them concurrently. The total runtime is closer to that of the single longest-running task. 
# Note: The aiohttp library is required for asynchronous HTTP requests (pip install aiohttp). 

import asyncio
import time
import aiohttp

async def fetch_async(session, url):
    print(f"Fetching {url}...")
    async with session.get(url) as response:
        print(f"Done fetching {url} with status code {response.status}")

async def main_async():
    start = time.perf_counter()
    urls = ['https://httpbin.org/delay/1', 'https://httpbin.org/delay/2']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, url) for url in urls]
        await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"Asynchronous execution time: {end - start:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main_async())

# Expected output: ~2.00 seconds (only as long as the longest wait)

# When to use asyncio
# asyncio is not always the right tool for the job. You should use it when your program is: 
# I/O-bound: The application spends most of its time waiting for input/output operations. This is the primary use case for asyncio.
# High-concurrency: You need to manage a large number of simultaneous tasks. The overhead of creating and switching between many coroutines is far lower than with threads.
# High-level network code: Building things like web servers, web clients, or APIs that handle a lot of requests at once.


# When to use alternatives
# Threading: For I/O-bound tasks where asyncio-compatible libraries are not available, or for background operations. Due to the Global Interpreter Lock (GIL), threading is not effective for CPU-intensive work.
# Multiprocessing: For CPU-bound tasks that require heavy computation and need to be parallelized across multiple processor cores. The overhead of creating a new process is significant, but it completely bypasses the GIL. 