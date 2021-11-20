import threading
from threading import Timer
import time
import sys

"""Print 500 until event is set (timer expires), then
   print 200

   Useful for mock testing eventually alive endpoints
"""


def task1(event, timeout=None):
    # Started thread but waiting for timer to set event...
    event_set = event.wait(timeout)

    if event_set:
        # Event received, releasing thread...
        print(200)


def task2(event, timeout=None):
    while event.isSet() is False:
        print("500")
        time.sleep(0.1)


def setEvent(event):
    event.set()


if __name__ == "__main__":
    try:
        event = threading.Event()
        thread1 = threading.Thread(target=task1, args=(event,))
        thread1.start()

        thread2 = threading.Thread(target=task2, args=(event,))
        thread2.start()

        Timer(3.0, setEvent, args=(event,)).start()
    except KeyboardInterrupt:
        print("\nexiting...")
        sys.exit(0)

# See
# - https://docs.python.org/3/library/threading.html#threading.Event
# - https://www.studytonight.com/python/python-threading-event-object
