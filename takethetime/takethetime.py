from typing import Optional

from time import time
from datetime import timedelta

n = 0


class takethetime:
    """A context manager for timing code"""

    def __init__(self, name: Optional[str]=None, echo: bool=True):
        global n
        n += 1

        self.label = name if name else "#" + str(n)
        self.echo = echo

    def __enter__(self):
        self._start = time()
        self._laps = []
        return self

    def __exit__(self, *args):
        self._end = time()
        if self.echo:
            print("{}\n - Total duration: {}".format(self.label, timedelta(seconds=self.duration)))
            if self._laps:
                durations_since_start = self.laps_duration_since_start()
                lap_durations = self.lap_durations

                # Print average lap time
                print(" - Average:", timedelta(seconds=self._avg_duration(lap_durations)))

                # Print each lap
                for i, time_since_start in enumerate(durations_since_start):
                    print(" - Lap #{}: {} (+{})".format(i, timedelta(seconds=time_since_start), timedelta(seconds=lap_durations[i])))

    def lap(self):
        self._laps.append(time())

    def laps_duration_since_start(self):
        # Print the average
        laps_duration_since_start = list(map(lambda l: l - self._start, self._laps))
        assert len(laps_duration_since_start) == len(self._laps)
        return laps_duration_since_start

    @staticmethod
    def laps_times_to_durations(laps):
        return list(map(lambda lpair: lpair[1] - lpair[0], zip(laps[:-1], laps[1:])))

    @property
    def laps(self):
        return self._laps

    @property
    def lap_durations(self):
        return self.laps_times_to_durations([self._start] + self._laps)

    @staticmethod
    def _avg_duration(durations):
        return sum(durations) / len(durations)

    @property
    def avg_duration(self):
        return self._avg_duration(self.lap_durations)

    @property
    def duration(self):
        return self._end - self._start
