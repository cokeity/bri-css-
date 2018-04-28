import sys, colors, pygame

class TAB (object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.tab = pygame.Surface((width,height))
		self.offset = 30 # how wide is the tabbar
		self.init_tab()

	def init_tab(self):
		#self.tab.fill(colors.MINTGREEN())
		#create HTML 
		self.html = pygame.Surface((self.width, self.height-self.offset))
		self.html.fill(colors.BLUE())
		#create CSS tab
		self.css = pygame.Surface((self.width, self.height-self.offset))
		self.css.fill(colors.RED())
		self.tab.blit(self.css,(0,self.offset))
		#create tab controller
		self.tab_control = pygame.Surface((self.width,self.offset))
		self.tab_control.fill(colors.MINTGREEN())
		self.tab.blit(self.tab_control,(0,0))

		self.tab.blit(self.html,(0,self.offset)) #shows html first 

	def show_css(self):
		self.tab.blit(self.css,(0,self.offset))

	def show_html(self):
		self.tab.blit(self.html,(0,self.offset))

	def get_tabsurface(self):
		return self.tab

	def redrawTab():
		pass
