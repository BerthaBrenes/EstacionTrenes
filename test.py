
import pygame
from pygame.locals import *

from GIF import GIF

def main():
    pygame.init()
    tren = GIF("Imagenes/5Tren.gif")
    screen = pygame.display.set_mode((tren.getWidth(), tren.getHeight()))
    for i  in range(10):
        while tren.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return
            tren.render(screen, (0, 0))
            pygame.display.flip()

if __name__ == "__main__":
    main()
