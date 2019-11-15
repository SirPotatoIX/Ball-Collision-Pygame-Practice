import pygame,sys
pygame.init()

screen_x = 800
screen_y = 400
screen = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption(("Uh oh, stinky!"))

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill ((100,100,100))
pygame.key.set_repeat(1)

box_lw = 69

box = pygame.Surface((box_lw,box_lw))
box = box.convert()
box.fill((69,69,255))

box2 = pygame.Surface((2*(box_lw), 2*(box_lw)))
box2 = box.convert()
box2.fill((200,100,150))

box_x = 0
box_y = 0
box_2_x = 300
box_2_y = 150


###
#Super important stuff
clock = pygame.time.Clock()
keepgoing = True
#Main loop
while keepgoing:
    #Refresh rate
    clock_rate = (60)
    clock.tick(clock_rate)

#Without this part, Windows freaks out and you won't be able to x out of the window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepgoing = False
            pygame.display.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i():
                print("e")



    box_x += 15
    if box_x > screen.get_width():
        box_x = (-box_lw)
        box_y += (box_lw)
    if box_y > screen.get_height():
        box_y = 0


    box_2_x -= 5
    if box_2_x < screen.get_width():
        box_2_x = (box_lw)
        box_2_y -= (box_lw)
    if box_2_y < 0:
        box_2_y = 80

###
    #Refresh the screen!
    screen.blit(background,(0,0))
    screen.blit(box, (box_x, box_y))
    screen.blit(box2, (box_2_x, box_2_y))
    pygame.display.flip()
