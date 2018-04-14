import sys, pygame, colors
from tab import TAB

class GUI(object):
    def init(self):
        pass

    def mousePressed(self, x, y):
        print("%d %d" %(x,y));

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        pass
        

    def redrawAll(self, screen):
        pass

    def __init__(self, fps=50, title="bri{css}"):
        self.fps = fps
        self.title = title
        pygame.init()

    #@TODO make width and height resizable 
    def run(self, WIDTH = 1000, HEIGHT = 500): 
        clock = pygame.time.Clock()
        # self.screen is the main Surface we're working with 
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #,HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.screen.fill(colors.WHITE())
        #self.tab = pygame.Surface((500,500))
        self.tabs = TAB(500,500)
        #self.tab.fill(colors.BLUE())
        self.screen.blit(self.tabs.get_tabsurface(),(500,0))
        #self.screen.fill((0,0,255))
        pygame.display.update()
        #self.tab.blit(self.screen,(500,0))
        #self.screen.blit(self.tab,(0,0))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        # self.init()
        isRunnning = True
        while isRunnning:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    isRunnning= False
            #self.screen.fill(self.bgColor)
            #self.redrawAll(self.screen)

        pygame.quit()