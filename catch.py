from pygame import *
window = display.set_mode((800,600))
display.set_caption("Catch")
background = transform.scale(image.load("img.jpg"),(800,600))
sprite = transform.scale(image.load("images (1).jfif"),(100,100))
clock = time.Clock()
FPS = 60
x1 = 0
y1 = 0
game = True
while game:
    window.blit(background, (0, 0))
    window.blit(sprite,(x1, y1))
    for e in event.get():
        if e.type == QUIT:
            game = False
    key_pressed = key.get_pressed()
    if key_pressed[K_LEFT] and x1 > 5:
        x1 -= 5
    if key_pressed[K_RIGHT] and x1 < 695:
        x1 += 5
    if key_pressed[K_UP] and y1 > 5:
        y1 -= 5
    if key_pressed[K_DOWN] and y1 < 495:
        y1 += 5
    clock.tick(FPS)
    display.update()