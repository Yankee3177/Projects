import sys, pygame
pygame.init()

size = width, height = 1000, 500
speed = [1, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
background = pygame.image.load("background.gif").convert()
ball = pygame.image.load("ball.gif")
scaleW = 50
scaleH = 150
ballrect = ball.get_rect()
#screen.blit(background, (0, 0))
pygame.transform.scale(ball,(scaleW,scaleH))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    pygame.transform.scale(ball,(scaleW-10,scaleH))
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.update()
# from pygame import QUIT
#
# pygame.init()
# DISPLAY= pygame.display.set_mode((500,400))
#
# WHITE=(255,255,255)
# BLUE=(0,0,255)
#
# DISPLAY.fill(WHITE)
#
# pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))#X,Y,height,width
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.flip()
