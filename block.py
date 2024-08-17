import pygame

class Block:

    def __init__(self, color, pos) -> None:
        self.color = color
        self.pos = pos
        self.rect = pygame.Rect(self.pos[0], self.pos[1], 100, 100)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
    
    def get_rect(self):
        return self.rect
    
    def get_color(self):
        return self.color
    
    def change_color(self, dot_color):
        if dot_color == (0, 0, 0):  # Black dot
            if self.color == (0, 0, 0):
                self.color = (250, 250, 195)  # Change to black
                return True
        elif dot_color == (250, 250, 195):  # White dot
            if self.color == (250, 250, 195):
                self.color = (0, 0, 0)  # Change to white
                return True
        return False
        