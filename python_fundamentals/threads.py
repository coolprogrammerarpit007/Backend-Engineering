import time
# from helpers import do_something,DoSomething
from Number import NumberPrinter
from image_downloading_project import ImageDownloader
import threading
# start = time.perf_counter()



# if __name__ == "__main__":
#     print(f"Thread name is {threading.current_thread().name} with id {threading.get_ident()}")
#     t1 = threading.Thread(target=do_something,args=["Arpit Mishra"])
#     t2 = threading.Thread(target=do_something, args =[ "Priyanshu Jangid"])
#     t3 = threading.Thread(target=do_something, args =[ "Avinash Kmawat"])
#     t1.start()
#     t2.start()
#     t3.start()
#     t1.join()
#     t2.join()
#     t3.join()
#     finish = time.perf_counter()
#     time_count = finish - start
#     print(f"\nTotal Time to RUN: {time_count:.1f} seconds")
    
    
    # difference b/w start and run method in threading
    # when thread is called using start then multiple threads will be called
    # when thread is called using run then only single thread is created
    
    
# if __name__ == "__main__":
#     t1 = DoSomething("Arpit")
#     t1.start()
#     t2 = DoSomething("Harshit")
#     t2.start()
#     t1.join()
#     t2.join()
        
    
    
   
    
# if __name__ == "__main__":
#     threads = []
#     for i in range(1,101):
#         thread = NumberPrinter(i)
#         thread.start()
#         threads.append(thread)
        
#     for thread in threads:
#         thread.join()



    