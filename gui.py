import sys, pygame

class GUI(object):
    #def init(self):

    def __init__(self, width=600, height=600, fps=50, title="Alex User Response"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        pygame.init()

    def run(self):
        clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.width, self.height))#,HWSURFACE|DOUBLEBUF|RESIZABLE)
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        #self.init()
        isRunnning = True
        while isRunnning:
            time = clock.tick(self.fps)
            #self.timerFired(time)
            for event in pygame.event.get():
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #     self.mousePressed(*(event.pos))
                # elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                #     self.mouseReleased(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons == (0, 0, 0)):
                #     self.mouseMotion(*(event.pos))
                # elif (event.type == pygame.MOUSEMOTION and
                #       event.buttons[0] == 1):
                #     self.mouseDrag(*(event.pos))
                # elif event.type == pygame.KEYDOWN:
                #     self._keys[event.key] = True
                #     self.keyPressed(event.key, event.mod)
                # elif event.type == pygame.KEYUP:
                #     self._keys[event.key] = False
                #     self.keyReleased(event.key, event.mod)
                # el
                if event.type == pygame.QUIT:
                    isRunnning= False
            #self.screen.fill(self.bgColor)
            #self.redrawAll(self.screen)

        pygame.quit()
