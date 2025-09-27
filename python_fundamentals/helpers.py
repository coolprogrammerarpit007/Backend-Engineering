import time
import threading


# Passing arguments to threads

def do_something(person_name):
    print(f"Thread name is {threading.current_thread().name} with id {threading.get_ident()}")
    print(f"******* Doing Something For The Person {person_name} ********")
    time.sleep(2)
    print("******* Done Something  ********")
    
    
    
 # creating threads using classes
 
 
# class DoSomething(threading.Thread):
#     def __init__(self, person_name):
#         # super().__init__()
#         self.person_name = person_name 
#         threading.Thread.__init__(self)
    
#     def run(self):
#         print(f"Thread name is {threading.current_thread().name} with id {threading.get_ident()}")
#         print(f"******* Doing Something For The Person {self.person_name} ********")
#         time.sleep(2)
#         print("******* Done Something  ********")
    
        
     