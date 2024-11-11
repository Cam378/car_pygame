import pygame
WHITE = (255, 255, 255)
'''
Author: Tyler Ustrzycki
Name: Car (extends pygame Sprite)
Description: pygame object of type sprite that draws a recangle and has the ability to move around the pygame screen
Initialization Parameters: color (RGB value), width, height (both wdinteger values)

'''
class Car(pygame.sprite.Sprite):
   #This class represents a car. It derives from the "Sprite" class in Pygame.
   def __init__(self, color, width, height):
       # Call the parent class (Sprite) constructor
       super().__init__()
       # Pass in the color of the car, and its x and y position, width and height.
       # Set the background color and set it to be transparent
       self.image = pygame.Surface([width, height])
       self.image.fill(WHITE)
       self.image.set_colorkey(WHITE)
       # Draw the car (a rectangle!)
       pygame.draw.rect(self.image, color, [0, 0, width, height])
      
       # Instead we could load a proper pciture of a car...
       # self.image = pygame.image.load("car.png").convert_alpha()
       # Fetch the rectangle object that has the dimensions of the image.
       self.rect = self.image.get_rect()

   '''
   Name: MoveRight, MoveLeft
   Description: Moves the x position of the sprite's rectangle and surface a certain number of pixels
   Parameters: 1 argument, pixels, should be an integer

   '''
   def moveRight(self, pixels):
    self.rect.x += pixels
  
   def moveLeft(self, pixels):
      self.rect.x -= pixels


   def moveRight(self,pixels,max_x):
     new_x = self.rect.x+pixels
     if new_x>=max_x:
       self.rect.x = max_x-10
     else:
       self.rect.x = new_x
   def moveLeft(self,pixels,min_x):
     new_x = self.rect.x-pixels
     if new_x<=min_x:
       self.rect.x = min_x
     else:
       self.rect.x = new_x
 
   '''
   Name: MoveUp, MoveDown
   Description: Moves the y position of the sprite's rectangle and surface a certain number of pixels
   Parameters: 1 argument, pixels, should be an integer

   '''
   def moveUp(self,pixels):
      self.rect.y -= pixels
   
   def moveDown(self,pixels):
      self.rect.y += pixels
