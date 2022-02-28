import sys, pygame
pygame.init()

FPS = 100
size = width, height = 1100, 600
speed = [1,0]
screen = pygame.display.set_mode(size)
BLACK = [0, 0, 0]
WHITE = [255,255,255]
BLUE = [0, 0, 255]
STARTPOSX = 250
STARTPOSY = 250
STARTRAD = 150.0
start = True



clock = pygame.time.Clock()


posX = 250
posY = 250
rad = 150.0
secRad = 0.0
lineX = 250
lineY = 399
lineLength = 750
background = pygame.image.load("background.gif")
background = pygame.transform.scale(background, (width*3,height*3))
moveB = -2100.0


while 1:

    clock.tick(FPS)
    screen.fill(WHITE)



    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if rad <= 1:#Circle is getting bigger
        if posX == STARTPOSX:#Reset the circle to loop again
            rad = STARTRAD
            secRad = 0.0
        else:
            moveB -= 2.5
            screen.blit(background, (moveB, 0))
            posX += -speed[0]
            posY -= 0.2
            secRad += 0.2
            lineX -= 1
            lineLength += 1

            pygame.draw.rect(screen, BLACK, (lineX, lineY, lineLength, 2))
            secCircle = pygame.draw.circle(screen, BLUE, (posX, posY), secRad,)


    else:#Circle is getting smaller
        posX += speed[0]
        posY += 0.2
        rad -= 0.2
        lineX += 1
        lineLength -= 1
        moveB += 2.5
        screen.blit(background, (moveB, 0))
        pygame.draw.circle(screen, BLUE, (posX, posY), rad)
        pygame.draw.rect(screen, BLACK, (lineX, lineY, lineLength, 2))
    pygame.display.flip()



