import unittest
from game_loops.memory_game import MemoryGame

class TestCreateGrid(unittest.TestCase):

    def setUp(self):
        self.memory_game = MemoryGame()

    def test_correct_amount_of_images(self):
        self.assertEqual(len(self.memory_game.tiles_group), 12)

    def test_tile_pairs(self):
        self.assertEqual(len(set(self.memory_game.cats)), 6)

    

    
