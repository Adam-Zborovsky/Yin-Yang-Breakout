import pygame 
import random
import math
import numpy

class Dot:

    def __init__(self, color, size, pos) -> None:
        self.color = color
        self.pos = pos
        self.heading = random.randint(0,360)

        if color == (0,0,0):
            image = pygame.image.load("images/black.png")
        if color == (250, 250, 195):
            image = pygame.image.load("images/white.png")
        self.dot_img = pygame.transform.scale(image, size)


    def get_color(self):
        return self.color

    def draw(self, screen):
        screen.blit(self.dot_img, self.pos)


    def move(self, speed):
        heading_rad = math.radians(self.heading)
        dx = speed * math.cos(heading_rad)
        dy = - speed * math.sin(heading_rad)
        self.pos[0] += dx
        self.pos[1] += dy


    def check_collision(self, blocks):
        image_rect = self.dot_img.get_rect(topleft=(self.pos[0], self.pos[1]))
        heading = self.heading

        if image_rect.left <= 0 or image_rect.right >= 800:
            heading = 180 - heading
        if image_rect.top <= 0 or image_rect.bottom >= 800:
            heading = - heading

        for row in blocks:
            for block in row:
                if image_rect.colliderect(block.get_rect()):
                    if(block.change_color(self.color)):
                        heading = 180 - heading
                        break 

        self.heading = heading
