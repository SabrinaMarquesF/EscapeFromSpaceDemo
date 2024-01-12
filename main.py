import os, sys

dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
###

import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
import random

pygame.init()

display = pygame.display.set_mode([840, 480])

pygame.display.set_caption("Escape from space")

#OO
ObjectGroup = pygame.sprite.Group()
asteroidGroup = pygame.sprite.Group()
shotGroup = pygame.sprite.Group()

#BackgroundSpace
bg = pygame.sprite.Sprite(ObjectGroup)
bg.image = pygame.image.load("data/asteroides.png")
bg.image = pygame.transform.scale(bg.image, [840, 480])
bg.rect = bg.image.get_rect()

player = Player(ObjectGroup)

#sound
pygame.mixer.music.load("data/OutThere.ogg")
pygame.mixer.music.play(-1)

shoot = pygame.mixer.Sound("data/Futuristic Assault Rifle Single Shot 01.wav")

gameLoop = True
gameover = False
timer = 20
clock = pygame.time.Clock()
if __name__ == "__main__":
    while gameLoop:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not gameover:
                    shoot.play()
                    newShot = Shot(ObjectGroup, shotGroup)
                    newShot.rect.center = player.rect.center

#Logic
        if not gameover:
            ObjectGroup.update()
            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.3:
                    newAsteroid = Asteroid(ObjectGroup, asteroidGroup)

            collisions = pygame.sprite.spritecollide(player, asteroidGroup, False, pygame.sprite.collide_mask)

            if collisions:
                print("Game over!")
                gameover = True

            hits = pygame.sprite.groupcollide(shotGroup, asteroidGroup, True, True, pygame.sprite.collide_mask)

 #Desenho
        display.fill([74, 67, 67])
        ObjectGroup.draw(display)
        pygame.display.update()