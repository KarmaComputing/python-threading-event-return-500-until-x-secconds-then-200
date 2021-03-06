import threading
from threading import Timer
import time
import sys

"""Print 500 until event is set (timer expires), then
   print 200

   Useful for mock testing eventually alive endpoints
"""

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

status_code = 500


@app.route("/")
def index():
    reset_timer()
    return render_template("wait.html")


@app.route("/wait")
def eventually_200():
    return f"{status_code}", status_code


@app.route("/reset")
def reset():
    """Reset timer to fake url returning 500 again until x secconds"""
    return redirect(url_for("index"))


def task1(event, timeout=None):
    # Started thread but waiting for timer to set event...
    event_set = event.wait(timeout)

    if event_set:
        # Event received, releasing thread...
        print(200)
        set_status_code(200)


def task2(event, timeout=None):
    while event.isSet() is False:
        print("500")
        time.sleep(0.1)


def setEvent(event):
    event.set()


def set_status_code(code=500):
    global status_code
    status_code = code


def reset_timer():
    try:
        set_status_code(500)
        event = threading.Event()
        thread1 = threading.Thread(target=task1, args=(event,))
        thread1.start()

        thread2 = threading.Thread(target=task2, args=(event,))
        thread2.start()

        Timer(3.0, setEvent, args=(event,)).start()
    except KeyboardInterrupt:
        print("\nexiting...")
        sys.exit(0)


reset_timer()


# See
# - https://docs.python.org/3/library/threading.html#threading.Event
# - https://www.studytonight.com/python/python-threading-event-object
