import pygame
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()


cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
image = cam.get_image()



cam.stop()
print("camera stopped")
