import pygame

class World:

    def __init__(self):
        self.blocks = []

        # create ground blocks
        for x in range(0, 800, 40):
            self.blocks.append((x, 500))

    def draw(self, screen):

        for block in self.blocks:
            pygame.draw.rect(screen, (139, 69, 19), (block[0], block[1], 40, 40))
