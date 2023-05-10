import os
import random
import pickle
import pygame
from sprites.tiles import Tiles

class MemoryGame:
    def __init__(self):

        self.tile_pairs = 6
        self.fps = 60
        self.saved_scores = []
        self.matched = []

        # timer
        self.start_time = pygame.time.get_ticks()
        self.timer_running = True
        self.saved_time = 0

        # getting the cat pictures
        self.all_cats = os.listdir(os.path.join(
            os.getcwd(), "src/pictures/cats"))
        self.image_width = 150
        self.image_height = 150
        self.borders = 5
        self.tiles_group = pygame.sprite.Group()

        # flipping and timing
        self.flipped = []
        self.block_game = False
        self.frame_count = 1
        self.create_grid()

    def create_grid(self):
        """Creates the grid with cat picture tiles.
        """
        self.cats = self.select_random_cats()
        self.generate_tiles(self.cats)

    def generate_tiles(self, cats):
        """Creates the level of the game, e.g. how many rows and
        columns of tiles there are.
        """
        n = len(cats)
        cols = min(n, 4)
        rows = (n + cols - 1) // cols

        # self.tiles_group.empty()

        for row in range(rows):
            for col in range(cols):
                i = row * cols + col
                if i >= n:
                    break
                x = col * (self.image_width + self.borders)
                y = row * (self.image_height + self.borders)
                tile = Tiles(cats[i], x, y)
                self.tiles_group.add(tile)

    def select_random_cats(self):
        """Selects a number of random pictures to use as the tiles 
        and multiplies it with two so there are matching pairs.
        Returns:
            A list of random cat pictures in a random order.
            """
        cats = random.sample(self.all_cats, self.tile_pairs)
        cats *= 2
        random.shuffle(cats)
        return cats

    def timer(self, screen):
        """Checks if timer is running and stops the time if it's not. 
        Stops the time is level is completed.
        Shows the timer on screen.
        Args:
            screen: display of the application
        """

        if self.timer_running:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        else:
            elapsed_time = self.saved_time // 1000

        if self.check_level_completion():
            if self.timer_running:
                self.saved_time = pygame.time.get_ticks() - self.start_time
                #self.saved_scores.append(self.saved_time//1000)

                #self.save_scores()
                self.timer_running = False

        timer_text = pygame.font.SysFont("gentium", 30).render(
            f"TIME: {elapsed_time}", True, (0, 0, 0))
        screen.blit(timer_text, (650, 10))

    def update(self, events, screen):
        """Args:
            events: list of events
            screen: display of application
        """
        self.user_input(events)
        self.draw(screen)
        self.timer(screen)
        self.level_completion(screen)

    def draw(self, screen):
        """Draws the tiles on a white screen.
        Args:
            screen: display of the application
        """
        screen.fill((255, 255, 255))

        self.tiles_group.draw(screen)
        self.tiles_group.update()

    def user_input(self, events):
        """Checks if game is blocked and forwards the actions to
        the appropriate method.
        Args:
            events: list of events
        """
        if not self.block_game:
            self.handle_mouse_clicks(events)
        else:
            self.handle_block_game()

    def handle_mouse_clicks(self, events):
        """Checks if user has clicked on the tiles.
        Args:
            events: list of events
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for tile in self.tiles_group:
                    if tile.rect.collidepoint(event.pos):
                        self.handle_tile_click(tile)

    def handle_tile_click(self, tile):
        """Shows clicked tile and checks if it is the second flipped tile.
        Args: 
            tile: game tile containing a picture of a cat
        """
        if tile.name not in self.matched:
            self.flipped.append(tile.name)
            tile.show()
            if len(self.flipped) == 2:
                self.handle_tile_pair()
        else:
            pass

    def handle_tile_pair(self):
        """Blocks the game if the flipped tiles aren't matching.
        """
        if self.flipped[0] != self.flipped[1]:
            self.block_game = True
        else:
            for tile in self.tiles_group:
                if tile.name == self.flipped[0]:
                    self.matched.append(tile.name)
            self.flipped = []

    def handle_block_game(self):
        """Waits for one second and flips the unmatching tiles back.
        """
        self.frame_count += 1
        if self.frame_count == self.fps:
            self.frame_count = 0
            self.block_game = False

            for tile in self.tiles_group:
                if tile.name in self.flipped:
                    tile.hide()
            self.flipped = []

    def check_level_completion(self):
        """Checks if the level is completed, i.e. all tiles are shown.
        Returns:
            True if the level is completed, otherwise False.
        """
        num_shown_tiles = sum(tile.shown for tile in self.tiles_group)
        return num_shown_tiles == len(self.tiles_group)

    def level_completion(self, screen):
        """Displays a message after the level is completed.
        """
        completion_text = pygame.font.SysFont(
            "gentium", 30).render("Congrats!", True, (0, 0, 0))

        if self.check_level_completion():
            screen.blit(completion_text, (300, 500))

    #def save_scores(self):
        """Saves the score (how much time used to complete level)
        """

        #with open("score.dat", "wb") as file:
        #    pickle.dump(self.saved_scores, file)
