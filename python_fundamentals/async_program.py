import asyncio


async def send_mail():
    print("Hello")
    
    
async def main():
    await send_mail()
    
    
if __name__ == "__main__":
     asyncio.run(main())