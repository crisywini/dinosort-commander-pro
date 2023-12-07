

import time
from watchdog.observers import Observer
from handler import Handler
 
 
class Watcher:

    def __init__(self, watch_directory='.'):
        self.observer = Observer()
        self.watch_directory = watch_directory
 
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watch_directory, recursive = True)
        self.observer.start()
        print("I am watching buddy")
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            print("Ok I got to sleep")
 
        self.observer.join()