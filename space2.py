from pygame import *

from random import randint
win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("space")
background = transform.scale(image.load("space-background-sololos (1).png"),(win_width,win_height))
mixer.init()
mixer.music.load("backgroundmusicforvideos-space-space-galaxy-universe-music-301239.mp3")
mixer.music.play()
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(img),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite ):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed
    def fire(self):
        pass
score = 0
lose = 0
font.init()
font1 = font.Font(None, 36)
text_lose = font1.render("Missed:"+ str(lose),True,(255, 255, 255))
text_score = font1.render("Score:"+ str(lose),True,(255, 255, 255))
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_height - 80)
            self.rect.y = 0
lose = lose + 1

monsters = sprite.Group()
for i in range(5):
    enemy = Enemy("download (1) (2).png",randint(0,win_width- 65), randint(-150,-40), 5)
    monsters.add(enemy)


player = Player("download (1) (3).png", 350, 430, 5)
enemy = transform.scale(image.load("space-background-sololos (1).png"),(65,65))
game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    monsters.draw(window)
    monsters.update()
    text_lose = font1.render("Missed:" + str(lose), True, (255, 255, 255))
    text_lose = font1.render("Score:" + str(lose), True, (255, 255, 255))
    window.blit(text_score, (10,10))
    window.blit(text_lose, (10,10))
    player.reset()
    player.update()
    clock.tick(FPS)
    display.update()
