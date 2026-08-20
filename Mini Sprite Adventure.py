import pygame

pygame.init()

screen_width = 400
screen_height = 400

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mini Sprite Adventure")

colors = {
    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white')
}

current_color = colors['white']

x, y = 100, 100
radius = 50

clock = pygame.time.Clock()

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]:
        x -= 3
    if pressed[pygame.K_RIGHT]:
        x += 3
    if pressed[pygame.K_UP]:
        y -= 3
    if pressed[pygame.K_DOWN]:
        y += 3


    x = min(max(radius, x), screen_width - radius)
    y = min(max(radius, y), screen_height - radius)

 
    if x == radius:
        current_color = colors['blue']
    elif x == screen_width - radius:
        current_color = colors['yellow']
    elif y == radius:
        current_color = colors['red']
    elif y == screen_height - radius:
        current_color = colors['green']
    else:
        current_color = colors['white']

    window.fill((0, 0, 0))

    pygame.draw.circle(window, current_color, (x, y), radius)

    pygame.display.update()
    clock.tick(90)

pygame.quit()





