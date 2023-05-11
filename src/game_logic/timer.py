import pygame


class Timer():
    """Class for the in-game timer.
    """
    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.timer_running = True
        self.saved_time = 0

    def update(self, screen):
        """Runs the timer and stops it at level completion.
        Draws the timer on screen.

        Args:
            screen: display of the application
        """
        if self.timer_running:
            elapsed_time = (pygame.time.get_ticks() - self.start_time) // 1000
        else:
            elapsed_time = self.saved_time // 1000

        timer_text = pygame.font.SysFont("gentium", 30).render(
            f"TIME: {elapsed_time}", True, (0, 0, 0))
        screen.blit(timer_text, (650, 10))
    