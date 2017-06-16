import pygame

display_width = 800
display_height = 600
pygame.init()
#setup ventanas
gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Tutorial Pygame")
clock = pygame.time.Clock()#reloj

robotImg = pygame.image.load('robot.gif')
def robot(x,y):
    gameDisplay.blit(robotImg,(x,y))
x = (display_width *0.65)
y =(display_height * 0.58)
x_change = 0
crashed = False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#cuando aparece la X de la ventana
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                x_change = -6
            if event.key == pygame.K_RIGHT:
                print("right")
                x_change = 6
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    #print(event)#se refirer a los eventos del teclado que se pueden usar 
    x += x_change
    gameDisplay.fill((34,255,255))
    robot(x,y)
    pygame.display.update() #muestra la ventana       
    clock.tick(60)

pygame.quit()
#quit()#genera un ventana para preguntar si quiere salirse del programa
