from typing import Optional

from time import time

n = 0


class TTT:
    """Take The Time, a context manager for timing code"""

    def __init__(self, label: Optional[str]=None, echo: bool=True):
        global n
        n += 1

        self.label = label if label else "#" + str(n)
        self.echo = echo

    def __enter__(self):
        self.start = time()
        self._laps = []
        return self

    def __exit__(self, *args):
        self.end = time()
        if self.echo:
            print("{}\n - Total duration: {}".format(self.label, self.duration))
            if self.laps:
                laps_duration = list(map(lambda l: l - self.start, self.laps))
                print(" - Average:", sum(laps_duration) / len(laps_duration))
                for i, lap in enumerate(self.laps):
                    print(" - Lap #{}: {}".format(i, lap))

    def lap(self):
        self._laps.append(time())

    @property
    def laps(self):
        return self._laps

    @property
    def duration(self):
        return self.end - self.start
