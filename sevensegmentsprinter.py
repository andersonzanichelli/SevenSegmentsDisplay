import sys

class SevenSegmentsPrinter:

    def __init__(self, *displays):
        self.displays = displays

    def show(self):
        display = ''

        for lista in self.displays:
            for d in lista:
                display += d.topLeft() + self.calcCenter(d.displaySize(), d.topCenter()) + d.topRight()
            display += '\n'

            for d in lista:
                display += d.midTopLeft() + self.calcCenter(d.displaySize(), d.midTopCenter()) + d.midTopRight()
            display += '\n'

            for d in lista:
                display += d.midLeft() + self.calcCenter(d.displaySize(), d.midCenter()) + d.midRight()
            display += '\n'

            for d in lista:
                display += d.midBottonLeft() + self.calcCenter(d.displaySize(), d.midBottonCenter()) + d.midBottonRight()
            display += '\n'

            for d in lista:
                display += d.bottonLeft() + self.calcCenter(d.displaySize(), d.bottonCenter()) + d.bottonRight()

        print display

    def calcCenter(self, size, segment):
        center = ''
        for x in xrange(1, size + 1):
            center += segment

        return center