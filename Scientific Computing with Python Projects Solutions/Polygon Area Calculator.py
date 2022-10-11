class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimetr(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ''
        for i in range(self.height):
            picture += '*'*self.width+'\n'
        return (picture)

    def get_amount_inside(self, obj):
        return (self.width//obj.width)*(self.height//obj.height)


class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width=width, height=width)

    def __repr__(self):
        return f"Square(side={self.width})"

    def set_side(self, width):
        self.width=width
        self.height=width

sq = Square(9)
# print(sq.get_area())
sq.set_side(4)
# print(sq.get_diagonal())
# print(sq.get_picture())




rect = Rectangle(10,5)
# print(shape.get_area())
# shape.set_height(4)
# print(shape.get_perimetr())
# print(shape.get_picture())
# sq = Square(9)
# print(sq)
print(rect.get_amount_inside(sq))
