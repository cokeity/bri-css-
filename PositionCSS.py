class PositionCSS:

    def __init__(name, position, left, top):
        self.name = name
        self.position = position
        self.left = left
        self.top = top

    def get_position:
        return position

    def get_left:
        return left

    def get_top:
        return top

    def update_y(top):
        self.top = top

    def update_x(left):
        self.left = left

    def to_css:
        return "<html>."+name+" {<br/>"+
            "&emsp;position: "+position+";<br/>"+
            "&emsp;left: "+left+";<br/>"+
            "&emsp;top: "+top+";<br/>"+
            "&emsp;width: "+WIDTH+";<br/>"+"}</html>"
