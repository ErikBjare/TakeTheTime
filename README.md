TakeTheTime
===========

Simple time taking library using context managers:

 - GitHub: https://github.com/ErikBjare/TakeTheTime
 - PyPI: https://pypi.python.org/pypi/TakeTheTime

## Example usage

Here follows some basic examples. For more, see the [examples](./examples) directory.

### Basic example

```python
from time import sleep
from takethetime import ttt

with ttt(name="Sleeping is boring, but effective"):
    sleep(0.1)                                     
```

```
Sleeping is boring, but effective
 - Total duration: 0:00:00.100140
```

### Using laps

```python
with ttt("You can't fill your lifetime need of sleep in one go") as t:
    for i in range(5):                                                
        sleep(0.02)                                                   
        t.lap()                                                       
```

```
You can't fill your lifetime need of sleep in one go
 - Total duration: 0:00:00.100489
 - Average: 0:00:00.020097
 - Lap #0: 0:00:00.020080 (+0:00:00.020080)
 - Lap #1: 0:00:00.040207 (+0:00:00.020127)
 - Lap #2: 0:00:00.060340 (+0:00:00.020133)
 - Lap #3: 0:00:00.080414 (+0:00:00.020073)
 - Lap #4: 0:00:00.100483 (+0:00:00.020069)
```

### Fetch results programatically

```python
t = ttt(echo=False)
with t:
    for i in range(3):
        sleep(0.1 * random())
        t.lap()
print(t.duration)
print(t.laps)
```
