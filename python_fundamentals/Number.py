import threading
import time

class NumberPrinter(threading.Thread):
    def __init__(self, number):
        self.number = number
        threading.Thread.__init__(self)
        
        
    def run(self):
        time.sleep(1)
        print(f"Number {self.number} printed by Thread name {threading.current_thread().name} with id {threading.get_ident()}")
