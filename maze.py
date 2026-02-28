from pygame import *

win_width = 700
win_height = 500

window = display.set_mode((win_width,win_height))
display.set_caption("M a z e")
background = transform.scale(image.load("img_4.png"),(win_width,win_height))
mixer.init()
mixer.music.load("jungle-nature-229896 (1).mp3")
mixer.music.play()
clock = time.Clock()
FPS = 60
speed = 5
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
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.x < win_height - 65:
            self.rect.y += self.speed
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 65:
            self.rect.x += self.speed

class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= win_width - 85:
            self.direction = "left"
        if self.direction == "left":
            self.rect.x -= self.speed
        if self.direction == "right":
            self.rect.x += self.speed
class Wall(sprite.Sprite):
    def __init__(self,color1,color2,color3,wall_x,wall_y,width,height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height= height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
w1 = Wall(119,119,0,100,20,10,350)
w2 = Wall(119,119,0,100,20,450,10)
w3 = Wall(119, 119, 0, 300, 20, 10, 350)
w4 = Wall(119, 119, 0, 100, 480, 450, 10)
w5 = Wall(119, 119, 0, 200, 100, 10, 380)
w6 = Wall(119, 119, 0, 100, 100, 10, 80)
sprite1 = GameSprite("download (1) (1) (1).png", 0 , 0, 5)
enemy = GameSprite("images (1).png", 470, 100, 5)
enemy2 = GameSprite("img_5.png", 470, 200, 5)

game = True
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()

    sprite1.update()
    sprite1.reset()
    enemy.update()
    enemy.reset()
    enemy2.update()
    enemy2.reset()
    clock.tick(FPS)
    display.update()

