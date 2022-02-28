import sys, pygame, random

def randomColor():
    BLACK = [0, 0, 0]
    BLUE = [0, 0, 255]
    RED = [255,0,0]
    YELLOW = [255,255,0]
    GREEN = [0,255,0]
    colors = [BLACK, BLUE, RED, YELLOW, GREEN]

    return colors[random.randrange(len(colors))]

def radAndLineText(x,y,radd,lengthLine):
    radiusText = font.render("This is the radius : " + str(radd), True, BLACK)
    lineText = font.render("This is the Length of the line : " + str(lengthLine), True, BLACK)
    screen.blit(radiusText, (x, y))
    screen.blit(lineText, (x, y+30))

pygame.init()

notReady = True
while notReady:
    STARTRAD = float(input("Enter the radius, the number must be between 50 and 160: "))
    if STARTRAD < 50 or STARTRAD > 160:
        print("Try again...")
    else:
        notReady = False
FPS = 100
clock = pygame.time.Clock()
size = width, height = 1100, 600
speed = [1,0]
screen = pygame.display.set_mode(size)
BLACK = [0, 0, 0]
WHITE = [255,255,255]


STARTPOSX = 250
STARTPOSY = 400-STARTRAD


rad = STARTRAD
posX = 250
posY = STARTPOSY
secRad = 0.0
lineX = 250
lineY = 399
lineLength = rad * 5
background = pygame.image.load("background.gif")
background = pygame.transform.scale(background, (width*3,height*3))
moveB = -2100.0
font = pygame.font.Font("freesansbold.ttf",25)
textPos = textX,textY = 0,height-150


color = randomColor()
while 1:

    clock.tick(FPS)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    if rad <= 1:#Circle is getting bigger
        if posX == STARTPOSX:#Reset the circle to loop again
            rad = STARTRAD
            secRad = 0.0
            color = randomColor()

        else:
            moveB -= 2.5
            screen.blit(background, (moveB, 0))
            posX += -speed[0]
            posY -= 0.2
            secRad += 0.2
            lineX -= 1
            lineLength += 1

            radAndLineText(textX,textY,secRad,lineLength)

            pygame.draw.rect(screen, BLACK, (lineX, lineY, lineLength, 2))
            secCircle = pygame.draw.circle(screen, color, (posX, posY), secRad, )


    else:#Circle is getting smaller
        posX += speed[0]
        posY += 0.2
        rad -= 0.2
        lineX += 1
        lineLength -= 1
        moveB += 2.5
        screen.blit(background, (moveB, 0))

        radAndLineText(textX, textY, rad, lineLength)
        pygame.draw.circle(screen, color, (posX, posY), rad)
        pygame.draw.rect(screen, BLACK, (lineX, lineY, lineLength, 2))

    pygame.display.flip()



