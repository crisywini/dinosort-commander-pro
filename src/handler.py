from watchdog.events import FileSystemEventHandler
import os
import shutil

class FileOrganizerHandler(FileSystemEventHandler):

    def __init__(self):
        self.executables_path = 'C:\\Users\\cristian.sanchezp\\Downloads\\executables'
        self.files_path = 'C:\\Users\\cristian.sanchezp\\Downloads\\files'
        self.wait_time = 300
        self.last_size = {}

 
 
    def on_modified(self, event):
        if event.is_directory:
            return
        
        file_path = event.src_path
        file_name = os.path.basename(file_path)
        print(f'File {file_name} is being modified')
        if file_name.endswith(('.tmp', '.crdownload', '.part')):
            print(f'Skipping temporary file: {file_name}')
            return

        new_path = os.path.join(self.executables_path, file_name) if file_name.endswith(".exe") or file_name.endswith(".msi") else  os.path.join(self.files_path, file_name)
        if os.path.exists(file_path):
            try:        
                shutil.move(file_path, new_path)
            except FileNotFoundError as fnf: 
                print(f'Error {fnf}')
            print(f'{file_name} saved')
        else: 
            print("skiping move")
        print(f'File {event.src_path} has been modified.')

    def on_created(self, event):
        print(f'New file: {event.src_path}')

    def on_deleted(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been deleted.')