import sys, colors, pygame

class TAB (object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tab = pygame.Surface((width,height))
		self.init_tab()

	def init_tab(self):
		offset = 30
		self.tab.fill(colors.MINTGREEN())
		#create HTML tab
		self.html = pygame.Surface((self.width, self.height-offset))
		self.html.fill(colors.BLUE())
		self.tab.blit(self.html, (0,offset))
		#create CSS tab

		#create tab controller
		

	def get_tabsurface(self):
		return self.tab

	def redrawTab():
		pass
