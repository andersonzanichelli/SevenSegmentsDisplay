import sys

class SevenSegmentsPrinter:

    def __init__(self, *displays):
        self.displays = displays

    def show(self):
        display = ''

        for lista in self.displays:
            for d in lista:
                display += d.topLeft() + d.topCenter() + d.topRight()
            display += '\n'

            for d in lista:
                display += d.midTopLeft() + d.midTopCenter() + d.midTopRight()
            display += '\n'

            for d in lista:
                display += d.midLeft() + d.midCenter() + d.midRight()
            display += '\n'

            for d in lista:
                display += d.midBottonLeft() + d.midBottonCenter() + d.midBottonRight()
            display += '\n'

            for d in lista:
                display += d.bottonLeft() + d.bottonCenter() + d.bottonRight()

        print display

    def test(self):
        print 'hello world!'