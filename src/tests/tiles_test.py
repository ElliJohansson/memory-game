import unittest
from create_grid import create_grid

class TestCreateGrid(unittest.TestCase):

    def setUp(self):
        self.grid = create_grid(2,2)
    
    def test_correct_amount_of_images(self):
        self.assertEqual(len(self.grid[1]), 4)