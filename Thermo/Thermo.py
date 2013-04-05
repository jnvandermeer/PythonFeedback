# we use pygame for our nice little thermometer!
import pygame

# let's try it...
class Thermo(object):
    """
    So... this class displays, using pygame, a nice thermometer on the
    screen. You can set the height of the thing as a percentage, using:
    set_percentage(some percentage)

    This is really just as simple as possible, and later should be
    integrated into pyff or pythonpy.
    """

    ## Just some base functions which I now overloaded. (French) Haha!
    # def __init__(self):
    #   pass

    # def __str__(self):
    #    pass

    # def __len__(self):
    #    pass

    def __init__(self):
        """
        This function should do the initialization, set all the right
        variables/screen size, etc etc.
        screen_size = a tuple with two int parameters.
        percentage = a float or int percentage number.
        It will also draw the screen, creating the surface
        And load/resize the images, etc.
        """
        screen_size = (1024, 768)
        percentage = 50.
        
        # self.screen_size = screen_size
        # self.percentage = percentage


        # get the screen surface!
        self.screen = pygame.display.set_mode(screen_size)

        
        # load my images...
        self.image_temperature = pygame.image.load("colorbar_morered.jpg").convert()
        self.image_thermometer = pygame.image.load("frame_greyblack_grad.bmp").convert()

        self.image_thermometer.set_colorkey((255, 255, 255))
        self.image_temperature.set_colorkey((255, 255, 255))

        # resizen thermometer...
        self.new_size_thermometer = (int(self.screen.get_size()[0]*0.2), int(self.screen.get_size()[1]*0.7))
        self.new_image_thermometer = pygame.transform.scale(self.image_thermometer,self.new_size_thermometer) 

        # resuzen temperature...
        self.new_size_temperature = (int(self.new_size_thermometer[0]*0.85), int(self.new_size_thermometer[1]*0.96))
        self.new_image_temperature = pygame.transform.scale(self.image_temperature,self.new_size_temperature)

        # what is the center of my screen?
        self.new_center = (self.screen.get_size()[0]*0.5, self.screen.get_size()[1]*0.5)

        # define the rects of where we would like to draw them!
        self.new_rect_thermometer = self.new_image_thermometer.get_rect()
        self.new_rect_temperature = self.new_image_temperature.get_rect()
        
        self.new_rect_thermometer.center=self.new_center
        self.new_rect_temperature.center=self.new_center

        # just do a small backup of our window for later use.
        self.temperature_window = self.new_rect_temperature


        # fill the screen...
        self.screen.fill((125,125,125))

        # get the background surface layer... the surface.. is the thing
        # that's constantly being updated.
        self.background=self.screen.copy()

        # put the thermometer on the screen.
        self.screen.blit(self.new_image_thermometer, self.new_rect_thermometer)

        # put the temperature also -- no, we don't have to yet... just set
        # it to some beginning position.
        # screen.blit(new_image_thermometer, new_rect_thermometer)

        # we don't update yet... that comes later.

        # with our complete set_percentage function... let's try calling that!
        self.set_percentage(percentage)
        

        # return self


    def set_percentage(self,percentage):
        """
        This function should update the termometer to some new value
        and then update the screen.
        """
        self.percentage = percentage
        p=self.percentage
        # print 'p = ' + str(p)

        # so what's the rect position of the temperature??
        oldpos = self.new_rect_temperature

        # get the new position... copy + change it.
        newpos = pygame.Rect(self.temperature_window)

        # change the offset + height..
        newpos[1]=self.temperature_window[1] + self.temperature_window[3] - self.temperature_window[3]/100.*p
        newpos[3]=self.temperature_window[3]/100.*p

        # we don't have to store the rects... but we CAN append them in an array..
        #
        dirty_rects = []
        dirty_rects.append(oldpos)
        dirty_rects.append(newpos)

        # we also need to change the rect encompassing the temperature surface to match.. so do it!
        # just use the temperature_window rect to change it... this
        # is a NEW rect that's made every time.
        sourcerect = pygame.Rect(self.temperature_window)
        sourcerect[0] = 0 # put the x at 0, xheight needs not to be changed.
        sourcerect[1] = self.temperature_window[3] - self.temperature_window[3]/100.*p
        sourcerect[3] = self.temperature_window[3]/100.*p

        # print 'oldpos = ' + str(oldpos)
        # print 'newpos = ' + str(newpos)
        # print 'sourcerect = ' + str(sourcerect)

        # so we've defined all our nice rects. Now we remove the bar... by copying background
        # material.
        self.screen.blit(self.background, oldpos, oldpos)

        # might as well draw also the thermometer ... again!!!.
        self.screen.blit(self.new_image_thermometer, self.new_rect_thermometer)


        # after that, we copy some stuff from the thermometer onto the screen...
        self.screen.blit(self.new_image_temperature,newpos,sourcerect)

        # we also update our temperature position...
        self.new_rect_temperature = newpos

        # and we update our screen while we're at it.
        pygame.display.flip()

        # we COULD have also done THIS:
        # pygame.display.update(dirty_rects)



    def stop(self):
        """
        Luckily, the stop keyword hasn't been used yet in python.
        I will use it for my class in order to stop the thing.
        ... only, I haven't got any idea yet how.
        """
        pygame.display.quit()
        



        

    def get_percentage(self):
        """    
        In case you were wondering where you set the bar to, this just returns
        the percentage value!
        """
        return self.percentage
