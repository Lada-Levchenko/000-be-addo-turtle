from abc import abstractmethod
from turtle import Turtle

t = Turtle()


class Figure(object):
    def __init__(self, **kwargs):
        super(Figure, self).__init__()
        self.x = t.position()[0]
        self.y = t.position()[1]
        self.color = t.color()[0]

    def _draw_decorator(self, function_to_decorate):
        def wrapper():
            t.setpos(self.x, self.y)
            t.color(self.color)
            t.down()
            t.begin_fill()

            function_to_decorate()

            t.end_fill()
            t.up()
        return wrapper

    @abstractmethod
    def _draw(self):
        """Draw some figure"""

    def draw(self):
        self._draw_decorator(self._draw)()


class Line(Figure):
    def __init__(self, **kwargs):
        super(Line, self).__init__(**kwargs)
        self.endX = kwargs["endX"]
        self.endY = kwargs["endY"]

    def _draw(self):
        t.goto(self.endX, self.endY)


class Rect(Figure):
    def __init__(self, **kwargs):
        super(Rect, self).__init__(**kwargs)
        self.width = kwargs["width"]
        self.height = kwargs["height"]

    def _draw(self):
        for i in range(2):
            t.forward(self.width)
            t.right(90)
            t.forward(self.height)
            t.right(90)


class Poly(Figure):
    def __init__(self, **kwargs):
        super(Poly, self).__init__(**kwargs)
        self.sides = kwargs["sides"]
        self.side_length = kwargs["side_length"]

    def _draw(self):
        angle = 360.0 / self.sides
        for i in range(self.sides):
            t.forward(self.side_length)
            t.right(angle)


class Circle(Figure):
    def __init__(self, **kwargs):
        super(Circle, self).__init__(**kwargs)
        self.radius = kwargs["radius"]

    def _draw(self):
        t.circle(self.radius)
