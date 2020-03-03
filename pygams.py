import pygame
 
FPS = 60
W = 300  # ширина экрана
H = 300  # высота экрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
play = True # Переменная для включения главного цикла
motion = 'STOP' # Переменная для движения круга
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
# координаты и радиус круга
x_start = W //2
y_start = H // 2
x = W // 2
y = H // 2
r = 10
while play:
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLUE, (x, y), r)
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            play = False
            pygame.quit()
            break
        elif i.type == pygame.KEYDOWN:
            _return = 0
            if i.key == pygame.K_LEFT:
                motion = 'LEFT'
            elif i.key == pygame.K_RIGHT:
                motion = 'RIGHT'
            elif i.key == pygame.K_UP:
                motion = 'UP'
            elif i.key == pygame.K_DOWN:
                motion = 'DOWN'
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                motion = 'STOP'
                _return = 1
    # Движение круга
    if motion == 'LEFT':
        x -= 3
        if x <= r:
            x = r
    elif motion == 'RIGHT':
        x += 3
        if x > W - r:
            x = W - r
    elif motion == 'UP':
        y -= 3
        if y <= r:
            y = r
    elif motion == 'DOWN':
        y += 3
        if y > H - r:
            y = H - r
        
    clock.tick(FPS)