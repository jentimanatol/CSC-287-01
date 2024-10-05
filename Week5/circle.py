from shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.rauis = radius


    def area(self):
        return self.radius *self.radius * 3.14
    
    def perimeter (self):
        return 2 * 3.14 * self.radius 