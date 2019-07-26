import threading
from threading import Thread

t = threading.current_thread()
print(t)


class PrintThread(Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


t1 = PrintThread()
t1.start()

c = threading.active_count()
print(f"Active Count : {c}")
