import pygame


class Timer():
    """Class for the in-game timer.
    """

    def __init__(self):
        self.start_time = pygame.time.get_ticks()
        self.timer_running = True
        self.saved_time = 0
        self.elapsed_time = 0

    def update(self):
        """Run the timer and stop it at level completion.
        """
        if self.timer_running:
            self.elapsed_time = (pygame.time.get_ticks() -
                                 self.start_time) // 1000
        else:
            self.elapsed_time = self.saved_time // 1000

    def draw_timer(self):
        """Create the timer text.

        Returns:
            Text containing the timer.
        """
        timer_text = pygame.font.SysFont("gentium", 30).render(
            f"TIME: {self.elapsed_time}", True, (0, 0, 0))

        return timer_text
