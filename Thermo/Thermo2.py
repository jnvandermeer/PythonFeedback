# we use pygame for our nice little thermometer!
import pygame
import socket
import sys

# let's try it...
class Thermo(object):
    """
    So... this class displays, using pygame, a nice thermometer on the
    screen. You can set the height of the thing as a percentage, using:
    set_percentage(some percentage)

    This is really just as simple as possible, and later should be
    integrated into pyff or pythonpy.
    """

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

        # do things with the event Que...
        self._eventQue = pygame.event
        # block empty events... and some other type (from documentation)
        # that's none and moisemotion, I guess??
        # maybe... this prevents pygame from crashing on windows computers
        # as according to:
        # http://www.pygame.org/docs/ref/event.html
        # the program should handle its events...
        self._eventQue.set_allowed(None)
        
        

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

        # or... do THIS
        pygame.display.update()
        # we COULD have also done THIS:
        # pygame.display.update(dirty_rects)

        # and now we need to make sure that the windows doesn't hang.

        # this will keep the thing in a never-ending loop.
        # so how do we prevent that (later on) in server mode?
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             raise SystemExit



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


    def server_mode(self):
        """
        This will put the Thermo in server mode. It will just listen to in-
        coming traffic. It should be an int between 0 and 100 that u send.
        You can also send a -1, and that will stop the server mode.
        The port number is 37201. *

        
        * 3720 to 1 are the odds of succesfully navigating an asteroid field (1).
        (1) Converging Evidence.
        """

        # what's our socket?
        server_address = ('localhost', 32701)

        print >>sys.stderr, 'starting up on %s port %s' % server_address


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(server_address)
        sock.listen(1)


        Setbreak=False
        while True:

            # use of a dummy variable... is this allright?? With a -1, the 'server' should stop!.
            if Setbreak:
                # print Setbreak
                # break out of THIS while loop...
                break

            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()

            # THIS is where the pygame is waiting
            # and where I should take good care of my
            # events otherwise windows will grow mad.
            # maybe just insert this to keep events rolling in?
            for event in self._eventQue.get():
                print event
                if event.type == pygame.QUIT:
                    raise SystemExit

            # print "bla"
            

            try:
                print >>sys.stderr, 'client connected:', client_address
                while True:
                    
                    data = connection.recv(16)

                    if data:

                        percentage = int(data)

                        print >>sys.stderr, 'received "%s"' % percentage
                        print 'I received a ' + str(percentage)

                        self.set_percentage(percentage)
                        
                        if percentage == -1:
                            print 'Breaking the connection!'
                            Setbreak=True

                    else:
                        break                    


            finally:
                connection.close()
