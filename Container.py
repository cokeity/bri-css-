class Container:

    def __init__(classname, position, left, top, element, page, x, y, width, height):
        self.classname = classname
        self.position = position
        self.left = left
        self.top = top
        self.element = element
        self.page = page
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.typeof = element.get_type()
        self.style = PositionCSS(classname, position, left, top)

    def get_classname():
        return self.classname

    def get_css_style():
        return self.style;

    def get_element():
        return self.element

    def to_html():
        if (self.type == 'header'):
            head = Header('enter text here', 'header')
            return "<html>&lt;div class=\""+self.classname+"\"&gt;<br/>"
            +"&emsp;"+head.to_html()+"<br/>"
            +"&lt;/div&gt;<br/></html>"
        elif (self.type == 'paragraph'):
            par = Paragraph("enter paragraph here", "paragraph")
            return "<html>&lt;div class=\""+self.classname+"\"&gt;<br/>"
            +"&emsp;"+par.to_html()+"<br/>"+"&lt;/div&gt;<br/></html>"
        elif (self.type == 'image'):
            Img = Image("enter image source here", "image")
            return "<html>&lt;div class=\""+self.classname+"\"&gt;<br/>"
            +"&emsp;"+Img.to_html()+"<br/>"+"&lt;/div&gt;<br/></html>"
        return ""

    def get_x():
        return self.x

    def get_y():
        return self.y

    def set_x(x):
        self.x = x

    def set_y(y):
        self.y = y

    def get_width():
        return self.width

    def get_height():
        return self.height
