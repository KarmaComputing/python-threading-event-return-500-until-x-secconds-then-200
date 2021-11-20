# Python event, threading , mock eventually ready

Print 500 until event is set (timer expires), then print 200.
Useful for mock testing eventually alive endpoints

# Usage
```
python3 -m venv vev
. venv/bin/activate
pip install Flask # flask is not required (see git tags)
./run.sh
```


## See also 

- https://docs.python.org/3/library/threading.html#threading.Event
- https://www.studytonight.com/python/python-threading-event-object
