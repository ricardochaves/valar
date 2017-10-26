import sys
import time
import uuid
import shutil
import os
from watchdog.observers import Observer  
from watchdog.events import PatternMatchingEventHandler

class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.xml", "*.lxml"]

    def process(self, event):
        """ 
        event.event_type 
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        print(event.src_path, event.event_type)  # print now only for degug
        uu = uuid.uuid4()
        print(uu)
        diretorio_destino = '/home/ricardo/projects/valar/xmls/dest/' + str(uu) + '/'
        print('diretorio_destino: ' + diretorio_destino)
        os.makedirs(diretorio_destino)
        dest1 = diretorio_destino + event.src_path.split('/')[1]
        print('dest1: ' + dest1)
        des = shutil.move(event.src_path, dest1)
        print('des: ' + des)

    # def on_modified(self, event):
    #     self.process(event)

    def on_created(self, event):
        self.process(event)

if __name__ == '__main__':
    print('Iniciando')
    args = sys.argv[1:]
    observer = Observer()
    observer.schedule(MyHandler(), path=args[0] if args else '.')
    print('observer.start()')
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()