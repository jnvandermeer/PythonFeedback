import pygame
import time

screen = pygame.display.set_mode((1024, 768))

new_center = (screen.get_size()[0]*0.5, screen.get_size()[1]*0.5)


running = True
# maybe first make the event que??
eventQue = pygame.event
# then setting some event type as blocked?
eventQue.set_blocked([0,4])


# load my images...
image_temperature = pygame.image.load("classifierbar.png").convert()
image_thermometer = pygame.image.load("frame_blue_grad.bmp").convert()

image_thermometer.set_colorkey((255, 255, 255))
image_temperature.set_colorkey((255, 255, 255))

# resizen die handel.
new_size_thermometer = (screen.get_size()[0]*0.2, screen.get_size()[1]*0.7)
new_image_thermometer = pygame.transform.scale(image_thermometer,new_size_thermometer)


new_size_temperature = (new_size_thermometer[0]*0.85, new_size_thermometer[1]*0.96)
new_image_temperature = pygame.transform.scale(image_temperature,new_size_temperature)

new_rect_thermometer = new_image_thermometer.get_rect()
new_rect_temperature = new_image_temperature.get_rect()
new_rect_thermometer.center=new_center
new_rect_temperature.center=new_center



# display something on the screen!
screen.fill((100,100,100))
background=screen.copy()

print screen
print background

# a fill supercedes it all..
print new_image_temperature
screen.blit(new_image_temperature, new_rect_temperature)
screen.blit(new_image_thermometer, new_rect_thermometer)

# screen.blit(background, new_rect_temperature, new_rect_temperature)


# print new_image_temperature.get_rect()

# copy oldpos rect...


# for p in percentage
# Show It!!
pygame.display.flip()

# get a pos which we can change at our will, depending on percentage!!
pos=pygame.Rect(new_rect_temperature)
newpos=pygame.Rect(new_rect_temperature)
print pos

for p in range(0,101,5):

    time.sleep(0.1)

    # create an empty list
    dirty_rects=[]

    pos=newpos
    # 1) blit rec rec.
    screen.blit(background, pos, pos)
    print 'pos = ' + str(pos)


    # 2) store rec array.
    dirty_rects.append(pos)

    # 3) change the rec thingy..
    newpos=pygame.Rect(pos)
    newpos[0]=pos[0]
    newpos[1]=new_rect_temperature[1] + new_rect_temperature[3] - new_rect_temperature[3]/100.*p
    newpos[2]=pos[2]
    newpos[3]=new_rect_temperature[3]/100.*p
    # print 'new_rect_thermometer = ' + str(new_rect_temperature)
    # print 'newpos = ' + str(newpos)

    # 4) copy again..
    dirty_rects.append(newpos)

    sourcerect = pygame.Rect(new_rect_temperature)
    sourcerect[0] = 0
    sourcerect[2] = new_rect_temperature[2]
    sourcerect[1] = new_rect_temperature[3] - new_rect_temperature[3]/100.*p
    sourcerect[3] = new_rect_temperature[3]/100.*p
    # print sourcerect[1]
    # print new_rect_temperature[3]
    print p
    print sourcerect
    
    # 5) blit it again!
    screen.blit(new_image_temperature,newpos,sourcerect)

    # print newpos
    # lastly, update the recs in my dirty_rec list!!!
    pygame.display.update(dirty_rects)
    

    pygame.display.flip()
    # print dirty_rects    
    


# print percentage
print new_rect_temperature

# screen.blit(new_image_thermometer, new_rect_thermometer)
# screen.blit(new_image_temperature, new_rect_temperature)
# pygame.display.flip()

# screen.blit(background, new_rect_temperature, new_rect_temperature)

# print background
# screen.blit(background,new_image_thermometer.get_rect())

# s=raw_input('press to continue..')


while running:

    # no idea yet what this does.
    # see reference p. 77.


    # use double-buffer??
    # yeah, bit somehow... it doesn't really be used in pyff. Why not?
    # See ref. page 13, 'updates' the display..    
    pygame.display.flip()


    # i will want to see what events are happening! keeping track of the mouse is one, for example.
    # see Reference, page no. 22.
    # maybe here??
    # managing the event subsystem, like a B.O.S.S.!!!
    
    eventQue.pump()
    event=eventQue.wait()
    #if event:
    print event

    # lets me close the window
    # see reference page no. 4.
    if event.type == pygame.QUIT:
        running = False


    
