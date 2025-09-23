import sys
from typing import final
import pygame


@final
class App:
    def __init__(self, width: int, height: int, title: str = "TITLE") -> None:
        pygame.init()
        self.__display = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title=title)
        self.__clock = pygame.time.Clock()
        self.__running = True

    def __update(self) -> None:
        pass

    def __draw(self) -> None:
        pass

    def __close(self) -> None:
        pygame.quit()
        sys.exit()

    def run(self):
        """
        runs an app with white background
        """
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display.fill("white")

            self.__update()
            self.__draw()

            pygame.display.flip()

        self.__close()

    @property
    def running(self) -> bool:
        """
        return False if window should close and True if not
        """
        return self.__running

    @running.setter
    def running(self, value: bool) -> None:
        """
        sets a new value to running
        If new value is False the windows shall close, if True window shall running
        """
        self.__running = value

    @property
    def display(self) -> pygame.Surface:
        """
        returns a window's display
        """
        return self.__display
