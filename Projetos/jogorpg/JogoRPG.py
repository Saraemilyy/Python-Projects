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

def message_to_screen(message, textfont, size, color):
 my_font = pygame.font.Font(textfont, size)
 my_message = my_font.render(message, 0, color)
 return my_message

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
gray = (50, 50, 50)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

for convert_sprites in sprite.all_sprites:
 convert_sprites.convert_alpha()

clock = pygame.time.Clock()
FPS = 60

player = helicopter.Helicopter = open(100, display_height/2-40)
moving = True 
godmode = False

score = 0 
highscore_file = open('highscore.dat', "r")
highscore_int = int(highscore_file.read())

cloud_x = 800
cloud_y = random.randint(0, 400)

enemy_heli = enemy_heli.EnemyHeli(-100, display_height/2-40)
enemy_feli_alive = False

boat = boat.Boat(-110, 430)
boat_alive = False

spaceship_x = 800
spaceship_y = random.randint(0, 400)
spaceship_alive = False
spaceship_hit_player = False
warning_once = True
warning = False
warning_counter = 0
warning_message = message_to_screen("!", font, 200, red)

balloon_x = 800
balloon_y = random.randint(0, 400)

bullets = []

bombs = []

shoot = pygamer.mixer.sound('JogoSan/sounds/shoot.way')
alert = pygamer.mixer.sound('JogoSan/sounds/alert.way')
bomb = pygamer.mixer.sound('JogoSan/sounds/bomb.way')
explosion = pygamer.mixer.sound('JogoSan/sounds/explosion.way')
explosion2 = pygamer.mixer.sound('JogoSan/sounds/explosion2.way')
pop = pygamer.mixer.sound('JogoSan/sounds/pop.way')
select = pygamer.mixer.sound('JogoSan/sounds/select.way')
select2 = pygamer.mixer.sound('JogoSan/sounds/select2.way')
whoosh = pygamer.mixer.sound('JogoSan/sounds/whoosh.way')

def main_menu():
 global cloud_x
 global cloud_y

 menu = True

 selected = "play"

 while menu:
  for event in pygame.event.get():
   if event.type == pygame.QUIT:
     pygame.quit()
   if event.type == pygame.KEYDOWN:
     if event.key == pygame.k_w or event.key == pygame.K_UP:
       pygame.mixer.Sound.play(select)
       selected = "play"
     elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
       pygame.mixer.Sound.play(select)
       selected = "play"
     if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
       pygame.mixer.Sound.play(select2)
       if selected == "play":
        menu = False
       if select == 'quit':
        pygame.quit()
        quit()

game_display.blit(sprites.background, (0, 0))
game_display.blit(sprites.cloud, (cloud_x, cloud_y))
if cloud_x <= 800 - 1100:
 cloud_x= 800
 cloud_y = random.randint(0, 400)
else:
 if not player.wreck_start:
   cloud_x -= 5
   if godmode:
    title = message_to_screen("HELICOPTERO (GODMODE)", font, 80, yellow)
   else:
    title = message_to_screen("HELICOPTERO", font, 100, black)

