import unittest
import pygame
from game_logic.memory_game import MemoryGame

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = MemoryGame()
        self.game.timer.start_time = 13000
        self.game.create_grid()

    def test_level_completion(self):
        for tile in self.game.tiles_group:
            tile.shown = True

        self.assertEqual(self.game.check_level_completion(), True)


    def test_stop_timer(self):
        for tile in self.game.tiles_group:
            tile.shown = True

        self.game.stop_timer()

        self.assertEqual(self.game.timer.timer_running, False)

    def test_saved_score(self):
        for tile in self.game.tiles_group:
            tile.shown = True
    
        self.game.timer.start_time = 13000
        self.game.stop_timer()

        self.assertEqual(self.game.saved_score, -13)

    def test_tile_click_with_one_tile(self):
        tile = self.game.tiles_group.sprites()[0]
        self.game.handle_tile_click(tile)

        self.assertEqual(len(self.game.flipped), 1)

    def test_tile_click_with_two_tiles(self):
        tile1 = self.game.tiles_group.sprites()[0]
        tile2 = None

        for tile in self.game.tiles_group.sprites():
            if tile.name != tile1.name:
                tile2 = tile
                break

        self.game.handle_tile_click(tile1)
        self.game.handle_tile_click(tile2)

        self.assertEqual(len(self.game.flipped), 2)

    def test_tile_match(self):
        self.game.flipped.append(self.game.tiles_group.sprites()[0])

        for tile in self.game.tiles_group:
            if tile.name == self.game.flipped[0].name and tile.id != self.game.flipped[0].id:
                self.game.flipped.append(tile)

        self.game.handle_tile_pair()

        self.assertEqual(len(self.game.flipped), 0)

    def test_not_matched_tiles(self):
        self.game.flipped.append(self.game.tiles_group.sprites()[0])

        for tile in self.game.tiles_group:
            if tile.name != self.game.flipped[0].name and len(self.game.flipped) < 2:
                self.game.flipped.append(tile)

        self.game.frame_count = 59
        self.game.handle_block_game()

        self.assertEqual(len(self.game.flipped), 0)
