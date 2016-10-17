import unittest
from time import sleep

from takethetime import ttt


class BasicTests(unittest.TestCase):
    def test_duration(self):
        t = ttt(echo=False)
        with t:
            sleep(0.1)
        self.assertTrue(0.1 < t.duration)
        self.assertTrue(t.duration < 0.11)

    def test_average(self):
        t = ttt(echo=False)
        with t:
            for i in range(5):
                sleep(0.05)
                t.lap()
        self.assertTrue(0.05 < t.avg_duration)
        self.assertTrue(t.avg_duration < 0.055)
