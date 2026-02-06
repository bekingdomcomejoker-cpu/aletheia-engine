import time, requests, os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ThroneSyncHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            with open(event.src_path, 'r') as f:
                content = f.read()
                print(f"📡 Pushing Truth: {event.src_path}")
                requests.post("https://aletheia-throne.onrender.com/classify", 
                              json={"content": content})

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(ThroneSyncHandler(), path="/storage/emulated/0/aletheia_inbox", recursive=False)
    observer.start()
    print("⚔️ Sovereign Sync Active (Head 5)")
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt: observer.stop()
