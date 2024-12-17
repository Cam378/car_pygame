import pygame

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Window size
width, height = 400, 400
screen = pygame.display.set_mode((width, height))

# Background color
background_colour = (0, 0, 0)

# Initialize pygame
pygame.init()

# Car class
class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.color = color  # Store the car's current color

    def update_color(self, color):
        self.color = color  # Update the car's color attribute
        self.image.fill(WHITE)  # Clear the surface
        pygame.draw.rect(self.image, color, [0, 0, self.rect.width, self.rect.height])

    def moveRight(self, pixels):
        if self.rect.x + pixels + self.rect.width <= width:
            self.rect.x += pixels

    def moveLeft(self, pixels):
        if self.rect.x - pixels >= 0:
            self.rect.x -= pixels

    def moveUp(self, pixels):
        if self.rect.y - pixels >= 0:
            self.rect.y -= pixels

    def moveDown(self, pixels):
        if self.rect.y + pixels + self.rect.height <= height:
            self.rect.y += pixels


# Create sprite group
all_sprites_list = pygame.sprite.Group()

# Create cars
playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

playerCar2 = Car(GREEN, 20, 30)
playerCar2.rect.x = 150
playerCar2.rect.y = 300

# Add cars to sprite group
all_sprites_list.add(playerCar)
all_sprites_list.add(playerCar2)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    collide = playerCar.rect.colliderect(playerCar2.rect)

    if collide:
        # Swap colors when cars collide
        temp_color = playerCar.color
        playerCar.update_color(playerCar2.color)
        playerCar2.update_color(temp_color)
    else:
        # Move cars based on user input
        if keys[pygame.K_LEFT]:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerCar.moveRight(5)
        if keys[pygame.K_UP]:
            playerCar.moveUp(5)
        if keys[pygame.K_DOWN]:
            playerCar.moveDown(5)
        if keys[pygame.K_a]:
            playerCar2.moveLeft(5)
        if keys[pygame.K_d]:
            playerCar2.moveRight(5)
        if keys[pygame.K_w]:
            playerCar2.moveUp(5)
        if keys[pygame.K_s]:
            playerCar2.moveDown(5)

    # Game logic
    all_sprites_list.update()

    # Fill background
    screen.fill(background_colour)

    # Draw all sprites
    all_sprites_list.draw(screen)

    # Update the display
    pygame.display.flip()

    pygame.time.delay(10)

# Quit pygame
pygame.quit()
