from watchdog.events import FileSystemEventHandler

class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_any_event(event):
        print(event)