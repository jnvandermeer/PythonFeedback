# here the stuff happens...

def update_classifier_bar(self, update_classifier=True):
        if update_classifier:
            class_out = self.calc_classifier()
        else:
            class_out = self.barX
        (barWidth, barHeight) = self.barSize
        if class_out > 0:
            self.barAreaRect = pygame.Rect(barWidth / 2, 0, class_out * barWidth / 2, barHeight)
            self.barRect = pygame.Rect(self.barCenter[0], self.barCenter[1] - barHeight / 2, class_out * barWidth / 2, barHeight)
        else:
            self.barAreaRect = pygame.Rect((1 + class_out) * barWidth / 2, 0, - class_out * barWidth / 2, barHeight)
            self.barRect = pygame.Rect(self.barCenter[0] + class_out * barWidth / 2, self.barCenter[1] - barHeight / 2, - class_out * barWidth / 2, barHeight)
        return class_out


# figure out how to draw stuff in python with this...
    def draw_all(self, drawall=False, drawhbs=False):
        """
        Draw current feedback state onto the screen.
        """
        self.screen.blit(self.background, self.backgroundRect)
        self.screen.blit(self.keeper, self.keeperMoveRect)
        self.screen.blit(self.bar, self.barRect, self.barAreaRect)
        self.screen.blit(self.frame, self.frameRect)
        self.screen.blit(self.tb1, self.tb1Rect)
        self.screen.blit(self.tb2, self.tb2Rect)
        self.screen.blit(self.fixl, self.fixlRect)
        self.screen.blit(self.fixr, self.fixrRect)
        self.screen.blit(self.fixb, self.fixbRect)
        if drawhbs:
            self.screen.blit(self.hbLeft, self.hbLeftRect)
            self.screen.blit(self.hbRight, self.hbRightRect)
        elif self.miss and self.showRedBallDuration >= self.hitMissElapsed and not self.continueAfterMiss:
            self.screen.blit(self.ball_miss, self.ballMoveRect)
        else:
            self.screen.blit(self.ball, self.ballMoveRect)
        if self.showCounter:
            s = self.hitstr + str(self.hitMissFalse[0]) + self.missstr + str(self.hitMissFalse[1]) + self.falsestr + str(self.hitMissFalse[ - 1])
            self.do_print(s, self.hitmissCounterColor, self.counterSize, self.counterCenter)
        if drawall or drawhbs:
            pygame.display.update()
        else:
            pygame.display.update([self.ballMoveRect, self.ballRect, self.barRect_init, self.keeperMoveRect, self.kMR, self.bMR, self.fixbRect])

# once I can draw some simple stuff on the screen, use psychopy and glob stuff.
# then move on to pyff!!

# draw a rectangle/window
# put inside the bar/draw something using this code/flip it.
# log stuff/psychopy?
# maybe even contact these people!
# listen to a port and update in main loop
# send changes in a directory over IP


