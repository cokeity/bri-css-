class Paragraph(HTMLelement):

	def __init__(self, type, text):
		self.text = text

	def get_type(self):
		return self.type

        def to_html():
            return "&lt;p&gt;<br/>" +
               "&emsp;" + self.text + "<br/>" +
               "&lt;/p&gt;<br/>";
