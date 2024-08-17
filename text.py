import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Create a surface for the blit (e.g., a sprite)
sprite = pygame.Surface((50, 50))
sprite.fill((255, 0, 0))  # Red color
sprite_rect = sprite.get_rect()
sprite_rect.topleft = (100, 100)  # Initial position

# Create a rectangle
rect = pygame.Rect(400, 300, 100, 80)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the sprite (for example purposes)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_rect.x -= 2
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += 2
    if keys[pygame.K_UP]:
        sprite_rect.y -= 2
    if keys[pygame.K_DOWN]:
        sprite_rect.y += 2
    
    # Check for collision
    if sprite_rect.colliderect(rect):
        print("Collision detected!")
    
    # Clear the screen
    screen.fill((255, 255, 255))  # White background
    
    # Draw the sprite and rectangle
    screen.blit(sprite, sprite_rect)
    pygame.draw.rect(screen, (0, 255, 0), rect)  # Green rectangle
    
    # Update the display
    pygame.display.flip()

pygame.quit()