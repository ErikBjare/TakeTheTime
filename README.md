TakeTheTime
===========

Simple time taking library using context managers:

 - GitHub: https://github.com/ErikBjare/TakeTheTime
 - PyPI: https://pypi.python.org/pypi/TakeTheTime

## Example usage

### Basic example

```python
from time import sleep
from takethetime import ttt

i = 0
with ttt(name="Sleeping is boring, but effective"):
    sleep(2)   
```

```
Sleeping is boring, but effective
 - Total duration: 2.0020899772644043
```

### Using laps

```python
from time import sleep
from takethetime import ttt

i = 0
with ttt("You can't fill your lifetime need of sleep in one go") as t:
    for i in range(10):
        sleep(0.1)
            t.lap()
```

### Fetch results programatically

```python
t = ttt(echo=False)
with t:
    for i in range(3):
        sleep(0.1)
        t.lap()
print(t.duration)
print(t.laps)
```


```
#2
 - Total duration: 1.0016279220581055
 - Average: 0.5509152412414551
 - Lap #0: 1476642860.950517
 - Lap #1: 1476642861.0507028
 - Lap #2: 1476642861.1508887
 - Lap #3: 1476642861.2510433
 - Lap #4: 1476642861.3512292
 - Lap #5: 1476642861.45138
 - Lap #6: 1476642861.551568
 - Lap #7: 1476642861.6516976
 - Lap #8: 1476642861.7518508
 - Lap #9: 1476642861.8519933
```
