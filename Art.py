'''Assignment 4 Part 3

Regression Testing

>>> config = ArtConfig(count=100,x=(200,1000))
>>> config.count == 100
True

>>> random = GenRandom(config)
>>> random.x <= 1000
True

>>> random.y <= 300
True
'''


import random
from typing import IO


class ArtConfig:
    """"ArtConfig Class"""
    def __init__(
        self,
        count: int = 1000,
        x: int = (0, 500),
        y: int = (0, 300),
        shape: tuple = (0, 1),
        rad: tuple = (0, 100),
        rx: tuple = (0, 30),
        ry: tuple = (0, 30),
        w: tuple = (10, 100),
        h: tuple = (10, 100),
        r: tuple = (0, 255),
        g: tuple = (0, 255),
        b: tuple = (0, 255),
        op: tuple = (0.0, 1.0)
    ) -> None:
        self.count = count
        self.x = x
        self.y = y
        self.shape = shape
        self.rad = rad
        self.rx = rx
        self.ry = ry
        self.w = w
        self.h = h
        self.r = r
        self.g = g
        self.b = b
        self.op = op


class Svg:
    """Svg Class"""
    def __init__(self, config: ArtConfig, fd: IO[str]) -> None:
        self.width: tuple = config.x
        self.height: tuple = config.y
        self.fd = fd

    def gen_svg(self, config: ArtConfig):
        """gen_svg method"""
        for __ in range(config.count):
            random: GenRandom = GenRandom(config)
            shape: Shapes = Shapes(random)
            shape.Draws(self.fd)

    def gen_table(self, config):
        """gen_table method"""
        print(
            f'{"CNT":>3} {"SHA":>3} {"X":>3} {"Y":>3} {"RAD":>3} {"RX":>3} {"RY":>3} {"W":>3} {"H":>3} {"R":>3} {"G":>3} {"B":>3} {"OP":>3}'
        )
        for __ in range(config.count):
            random: GenRandom = GenRandom(config)
            print(f'{__:>3} {random}')


class ProEpilouge:
    """"ProEpilouge Class"""
    TAB: str = "   "
    t: int = 0

    def __init__(self, file_name: str, window_title: str) -> None:
        self.__fnam: str = file_name
        self.__wintitle: str = window_title
        self.fd: IO[str] = open(file_name, "w")

    def close_html_file(self) -> None:
        '''close_html_file method'''
        self.fd.close()

    def write_html_comment(self, com: str) -> None:
        '''write_html_comment method'''
        ts: str = ProEpilouge.TAB * ProEpilouge.t
        self.fd.write(f'{ts}<!--{com}-->\n')

    def write_html_line(self, line: str) -> None:
        '''write_html_line method'''
        ts: str = ProEpilouge.TAB * ProEpilouge.t
        self.fd.write(f"{ts}{line}\n")

    def write_html_head(self) -> None:
        '''write_html_head method'''
        self.write_html_line("<html>")
        self.write_html_line("<head>")
        ProEpilouge.t += 1
        self.write_html_line(f"<title>{self.__wintitle}</title>")
        ProEpilouge.t -= 1
        self.write_html_line("</head>")
        self.write_html_line("<body>")
        ProEpilouge.t += 1

    def write_html_tail(self) -> None:
        '''write_html_tail method'''
        ProEpilouge.t -= 1
        self.write_html_line("</body>")
        self.write_html_line("</html")

    def open_svg_canvas(self, config: ArtConfig) -> Svg:
        '''open_svg_canvas method'''
        self.write_html_comment("Define SVG drawing box")
        self.write_html_line(
            f'<svg width="{config.x[1]}" height="{config.y[1]}">')
        ProEpilouge.t += 2
        return Svg(config, self.fd)

    def close_svg_canvas(self) -> None:
        '''close_svg_canvas method'''
        ProEpilouge.t -= 2
        self.write_html_line("</svg>\n")

    def make_svg(self, config: ArtConfig):
        #Used to avoid creating svg object in main and keep main cleaner
        svg: Svg = self.open_svg_canvas(config)
        svg.gen_svg(config)
        self.close_svg_canvas()


class GenRandom:
    """GenRandom Class"""
    def __init__(self, param: ArtConfig):
        self.x = self.__gen_int_in_range(param.x)
        self.y = self.__gen_int_in_range(param.y)
        self.shape = self.__gen_int_in_range(param.shape)
        self.rad = self.__gen_int_in_range(param.rad)
        self.rx = self.__gen_int_in_range(param.rx)
        self.ry = self.__gen_int_in_range(param.ry)
        self.w = self.__gen_int_in_range(param.w)
        self.h = self.__gen_int_in_range(param.h)
        self.r = self.__gen_int_in_range(param.r)
        self.g = self.__gen_int_in_range(param.g)
        self.b = self.__gen_int_in_range(param.b)
        self.op = self.__gen_float_in_range(param.op)

    def __str__(self) -> str:
        return f'{self.shape:>3} {self.x:>3} {self.y:>3} {self.rad:>3} {self.rx:>3} {self.ry:>3} {self.w:>3} {self.h:>3} {self.r:>3} {self.g:>3} {self.b:>3} {self.op:>3.1f}'

    def __gen_int_in_range(self, tup: tuple) -> int:
        """__gen_int_in_range method"""
        return random.randint(tup[0], tup[1])

    def __gen_float_in_range(self, tup: tuple) -> float:
        """__gen_float_in_range method"""
        return round(random.uniform(tup[0], tup[1]), 1)


class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def Draws(self, f: IO[str]):
        '''Draws method (Circle)'''
        ts: str = ProEpilouge.TAB * ProEpilouge.t
        line: str = f'<circle cx="{self.cx}" cy="{self.cy}" r="{self.rad}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></circle>'
        f.write(f"{ts}{line}\n")


class Rectangle:
    '''Rectangle Class'''
    def __init__(self, rect: tuple, col: tuple):
        self.x: int = rect[0]
        self.y: int = rect[1]
        self.width: int = rect[2]
        self.height: int = rect[3]
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]

    def Draws(self, f: IO[str]):
        '''Draws method (Rectangle)'''
        ts: str = ProEpilouge.TAB * ProEpilouge.t
        line: str = f'<rect x="{self.x}" y = "{self.y}" width="{self.width}" height="{self.height}" fill="rgb({self.red}, {self.green}, {self.blue})" fill-opacity="{self.op}"></rect>'
        f.write(f"{ts}{line}\n")


class Shapes:
    """Shapes Class"""

    #Super class that makes drawing shapes easier
    def __init__(self, random: GenRandom) -> None:
        self.shape = random.shape
        if (random.shape == 1):  # circle
            cir: tuple = (random.x, random.y, random.rad)
            col: tuple = (random.r, random.g, random.b, random.op)
            self.shape = Circle(cir, col)

        elif (random.shape == 0):  # rectangle
            rect: tuple = (random.x, random.y, random.w, random.h)
            col: tuple = (random.r, random.g, random.b, random.op)
            self.shape = Rectangle(rect, col)
        else:
            print("Shape Not Defined")
            self.shape = None

    def Draws(self, f: IO[str]):
        '''Draws method (Shapes)'''
        self.shape.Draws(f)


def main():
    '''main method'''
    hd: ProEpilouge = ProEpilouge("a432.html", "My Art")
    hd.write_html_head()
    hd.make_svg(ArtConfig(count=1000, x=(0, 1000), b=(0, 100)))
    hd.make_svg(ArtConfig(count=1000, y=(0, 500)))
    hd.write_html_tail()

