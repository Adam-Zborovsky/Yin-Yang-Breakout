from block import Block
from dot import Dot
import numpy as np
import time
import pygame
import random

SIZE = (800, 800)
BLACK = (0, 0, 0)
WHITE = (250, 250, 195)
SPEED = 2.5

blocks = np.array([  [Block(BLACK,[0,0]),Block(BLACK,[100,0]),Block(BLACK,[200,0]),Block(BLACK,[300,0]),Block(BLACK,[400,0]),Block(BLACK,[0,0]),Block(BLACK,[500,0]),Block(BLACK,[600,0]),Block(WHITE,[700,0])]
                    ,[Block(BLACK,[0,100]),Block(BLACK,[100,100]),Block(BLACK,[200,100]),Block(BLACK,[300,100]),Block(BLACK,[400,100]),Block(BLACK,[500,100]),Block(BLACK,[600,100]),Block(WHITE,[700,100])]
                    ,[Block(BLACK,[0,200]),Block(BLACK,[100,200]),Block(BLACK,[200,200]),Block(BLACK,[300,200]),Block(BLACK,[400,200]),Block(WHITE,[500,200]),Block(WHITE,[600,200]),Block(WHITE,[700,200])]
                    ,[Block(BLACK,[0,300]),Block(BLACK,[100,300]),Block(BLACK,[200,300]),Block(BLACK,[300,300]),Block(BLACK,[400,300]),Block(WHITE,[500,300]),Block(WHITE,[600,300]),Block(WHITE,[700,300])]
                    ,[Block(BLACK,[0,400]),Block(BLACK,[100,400]),Block(BLACK,[200,400]),Block(WHITE,[300,400]),Block(WHITE,[400,400]),Block(WHITE,[500,400]),Block(WHITE,[600,400]),Block(WHITE,[700,400])]
                    ,[Block(BLACK,[0,500]),Block(BLACK,[100,500]),Block(BLACK,[200,500]),Block(WHITE,[300,500]),Block(WHITE,[400,500]),Block(WHITE,[500,500]),Block(WHITE,[600,500]),Block(WHITE,[700,500])]
                    ,[Block(BLACK,[0,600]),Block(WHITE,[100,600]),Block(WHITE,[200,600]),Block(WHITE,[300,600]),Block(WHITE,[400,600]),Block(WHITE,[500,600]),Block(WHITE,[600,600]),Block(WHITE,[700,600])]
                    ,[Block(BLACK,[0,700]),Block(WHITE,[100,700]),Block(WHITE,[200,700]),Block(WHITE,[300,700]),Block(WHITE,[400,700]),Block(WHITE,[500,700]),Block(WHITE,[600,700]),Block(WHITE,[700,700])]
                    ], dtype=object)
dots = np.array([Dot(BLACK, (50,50), [625,625]), Dot(WHITE, (50,50), [125, 125])])

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Yin Yang Breakout')

def check_win():
    pre_blc = blocks[0][0]
    for row in blocks:
        for block in row:
            if pre_blc.get_color() != block.get_color():
                return [False, block.get_color()]
            pre_blc = block

    return [True, pre_blc.get_color()]

def draw_winner(color):
    font = pygame.font.Font('FiraSans-Black.ttf', 64)
    
    if color == (250, 250, 195):
        text = font.render("Black Won", True, (0, 0, 0), (250, 250, 195))
        screen.fill((250, 250, 195))
    if color == (0, 0, 0):
        text = font.render("White Won", True, (250, 250, 195), (0, 0, 0))
        screen.fill((0,0,0))
    textrec = text.get_rect()
    textrec.center = (400, 300)
    screen.blit(text, textrec)
    
    pygame.display.flip()


def draw_blocks(screen, blocks):
    for row in blocks:
        for block in row:
            block.draw(screen)


def add_dot(dots, color):
    pos = []
    for row in blocks:
        for block in row:
            if block.get_color() != color:
                pos = [block.get_rect().x, block.get_rect().y]

    return np.append(dots, Dot(color, (50,50), pos))

def remove_dot(dots, color):
    indexs = []
    for i, dot in enumerate(dots):
        if dot.get_color() == color:
            indexs.append(i)
    random.shuffle(indexs)
    return np.delete(dots, indexs[0])


def main_loop():
    global dots, blocks
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS: 
                    dots = add_dot(dots, BLACK) 
                if event.key == pygame.K_MINUS: 
                    dots = remove_dot(dots, BLACK)

                if event.key == pygame.K_1: 
                    dots = add_dot(dots, WHITE)
                if event.key == pygame.K_2: 
                    dots = remove_dot(dots, WHITE)

        draw_blocks(screen, blocks)
        for dot in dots:
            dot.check_collision(blocks)
            dot.move(SPEED)
            dot.draw(screen)

        winner = check_win()
        if winner[0]:
            draw_winner(winner[1])
            time.sleep(5)
            running = False


        pygame.display.flip()
        clock.tick(120)
        

if __name__ == '__main__':
    main_loop()
    pygame.quit()
