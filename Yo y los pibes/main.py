from pygame import *

back = (200, 255, 255)
window = display.set_mode((600, 500))
window.fill(back)
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

test = GameSprite('el Diabolo2.png', 200, 200, 4, 50, 50)
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    test.draw()
    display.update()
    clock.tick(120)