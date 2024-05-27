import pygame
import helicopter
import enemy_heli
import bot
import sprites
import random

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init

pygame.display.set_icon(sprites.icon)
display_width = 800
display_height = 600
game.display = pygame.display.set_mode((display_width, display_height))

font = "8-Bit-Madness.ttf"
