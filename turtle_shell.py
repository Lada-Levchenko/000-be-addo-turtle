import cmd
import turtle
import figures
from figures import t
import pickle


def main():
    my_cmd = TurtleShell()
    my_cmd.cmdloop(my_cmd.intro)


class TurtleDrawer(object):
    
    list_figures = []

    @staticmethod
    def setpos(x, y):
        t.up()
        t.setpos(x, y)
        t.down()
        
    @staticmethod
    def home():
        t.home()

    @staticmethod
    def line(end_x, end_y):
        new_line = figures.Line(endX=end_x, endY=end_y)
        new_line.draw()
        TurtleDrawer.list_figures.append(new_line)

    @staticmethod
    def circle(radius):
        new_circle = figures.Circle(radius=radius)
        new_circle.draw()
        TurtleDrawer.list_figures.append(new_circle)

    @staticmethod
    def rect(width, height):
        new_rect = figures.Rect(width=width, height=height)
        new_rect.draw()
        TurtleDrawer.list_figures.append(new_rect)

    @staticmethod
    def poly(sides, side_length):
        new_poly = figures.Poly(sides=sides, side_length=side_length)
        new_poly.draw()
        TurtleDrawer.list_figures.append(new_poly)

    @staticmethod
    def color(color_name):
        t.color(color_name)

    @staticmethod
    def reset():
        t.reset()
        del TurtleDrawer.list_figures[:]

    @staticmethod
    def bye():
        turtle.bye()

    @staticmethod
    def export_file(file_name):
        open(file_name, 'wb').write(pickle.dumps(TurtleDrawer.list_figures))

    @staticmethod
    def import_file(file_name):
        TurtleDrawer.list_figures = pickle.load(open(file_name, 'rb'))
        for figure in TurtleDrawer.list_figures:
            figure.draw()

    @staticmethod
    def close(window):
        if window.file:
            window.file.close()
            window.file = None


class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(TurtleDrawer) '
    file = None

    # ----- figure turtle commands -----
    def do_rect(self, arg):
        """Draw rectangle with given width and height:  RECT 50 60"""
        TurtleDrawer.rect(*parse(arg))

    def do_poly(self, arg):
        """Draw polygon with given number of sides and and side-length:  POLY 6 50"""
        TurtleDrawer.poly(*parse(arg))

    def do_line(self, arg):
        """Move turtle to an absolute position with changing orientation.  GOTO 100 200"""
        TurtleDrawer.line(*parse(arg))

    # ----- basic turtle commands -----
    def do_setpos(self, arg):
        """Move turtle to an absolute position without painting.  SETPOS 100 200"""
        TurtleDrawer.setpos(*parse(arg))

    def do_home(self, arg):
        """Return turtle to the home postion:  HOME"""
        TurtleDrawer.home()

    def do_circle(self, arg):
        """Draw circle with given radius an options extent and steps:  CIRCLE 50"""
        TurtleDrawer.circle(*parse(arg))

    def do_color(self, arg):
        """Set the color:  COLOR BLUE"""
        TurtleDrawer.color(arg.lower())

    def do_reset(self, arg):
        """Clear the screen and return t to center:  RESET"""
        TurtleDrawer.reset()

    def do_bye(self, arg):
        """Stop recording, close the t window, and exit:  BYE"""
        print('Thank you for using turtle')
        TurtleDrawer.close(self)
        TurtleDrawer.bye()
        return True

    # ----- record and playback -----
    def do_export(self, arg):
        """Save future commands to filename:  EXPORT rose.td"""
        TurtleDrawer.export_file(arg)

    def do_import(self, arg):
        """Playback commands from a file:  IMPORT rose.td"""
        TurtleDrawer.close(self)
        TurtleDrawer.import_file(arg)


def parse(arg):
    """Convert a series of zero or more numbers to an argument tuple"""
    return tuple(map(int, arg.split()))


if __name__ == "__main__":
    main()
