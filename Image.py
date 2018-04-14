class Image(HTMLelement):

	def __init__(self, type, src):
		self.src = src

	def get_type(self):
		return self.type

        def to_html():
            return "&lt;img src = "+ self.src +"&gt;&emsp;<br/>"
