import requests
import uuid
import threading



class ImageDownloader(threading.Thread):
    def __init__(self,url):
        self.url = url
        threading.Thread.__init__(self)
        
    def run(self):
        print(f"Image downloaded by the thread {threading.current_thread().name}")
        image = requests.get(self.url).content
        image_name = f"images/{str(uuid.uuid4())}.jpg"
        
        with open(image_name,"wb") as f_hand:
            f_hand.write(image)
            print("Image Downloaded")
            
image_downloader = ImageDownloader("https://media.gettyimages.com/id/137761002/photo/australia-v-india-fourth-test-day-3.jpg?s=612x612&w=gi&k=20&c=g_vwIDvZa8iFNlV_FHbpAndOHvDK-ENndvyuJaMJlz8=")
image_downloader.start()
image_downloader.join()
        
    
    