import unittest
import pygame
from game_logic.timer import Timer

class TestTimer(unittest.TestCase):

    def setUp(self):
        self.timer = Timer()
        self.timer.start_time = 8000

    def test_elapsed_time_when_running(self):
        self.timer.update()

        self.assertEqual(self.timer.elapsed_time, -8)

    def test_elapsed_time_when_paused(self):
        self.timer.timer_running = False
        self.timer.update()

        self.assertEqual(self.timer.elapsed_time, 0)