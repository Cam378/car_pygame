import pygame, random


#Let's import the Car Class
from car import Car
pygame.init()
GREEN = (100, 255, 200)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
        
SCREENWIDTH=400
SCREENHEIGHT=500

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
playerCar = Car(RED, 20, 30)
playerCar.rect.x = 200
playerCar.rect.y = 300

playerCar2 = Car(PURPLE, 20, 30)
playerCar2.rect.x = 100
playerCar2.rect.y = 100
# Add the car to the list of objects
all_sprites_list.add(playerCar)
all_sprites_list.add(playerCar2)
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
carryOn = True
while carryOn:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x: #Pressing the x Key will quit the game
                 carryOn=False
 
    keys = pygame.key.get_pressed()
    
    collide = playerCar.rect.colliderect(playerCar2.rect)
    if collide:
        playerCar.rect.x = 200
        playerCar.rect.y = 300
        playerCar2.rect.x = 100
        playerCar2.rect.y = 100
    else:
    
      if keys[pygame.K_LEFT]:
          playerCar.moveLeft(1,0)
      if keys[pygame.K_RIGHT]:
          playerCar.moveRight(1,400)
      if keys[pygame.K_UP]:
          playerCar.moveUp(1)
      if keys[pygame.K_DOWN]:
          playerCar.moveDown(1)
      if keys[pygame.K_a]:
          playerCar2.moveLeft(2,0)
      if keys[pygame.K_d]:
          playerCar2.moveRight(2,400)
      if keys[pygame.K_w]:
          playerCar2.moveUp(2)
      if keys[pygame.K_s]:
          playerCar2.moveDown(2)
    #Gamee Logic
    all_sprites_list.update()

    #Drawing on Screen
    screen.fill(GREEN)
    #Draw The Road
    pygame.draw.rect(screen, GREY, [40,000, 200,500])
    #Draw Line painting on the road
    pygame.draw.line(screen, WHITE, [140,0],[140,500],5)
    
    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)
    all_sprites_list.draw(screen)

    #Refresh Screen
    pygame.display.flip()

    # Create a clock
    clock = pygame.time.Clock()

    #Number of frames per secong e.g. 60
    clock.tick(60)