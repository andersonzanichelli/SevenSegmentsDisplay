import sys
import unittest
from contextlib import contextmanager
from StringIO import StringIO
from sevensegmentsdisplay import SevenSegmentsDisplay
from sevensegmentsprinter import SevenSegmentsPrinter

class TestSevenSegmentsPrinter(unittest.TestCase):

    def setUp(self):
        self.ssdOff = SevenSegmentsDisplay(1, [(' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' '), (' ', ' ', ' ')])
        self.held, sys.stdout = sys.stdout, StringIO()
    
    def test_output(self):
        printer = SevenSegmentsPrinter(self.ssdOff)
        printer.test()
        self.assertEquals(sys.stdout.getvalue(),'hello world!\n')

    def test_print_0(self):
        ssd_0 = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')])
        printer = SevenSegmentsPrinter([ssd_0])
        printer.show()
        self.assertEquals(sys.stdout.getvalue(),
            ' - \n' +
            '| |\n' +
            '   \n' +
            '| |\n' +
            ' - \n')

    def test_print_01(self):
        ssd_0 = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')])
        ssd_1 = SevenSegmentsDisplay(1, [(' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')])
        printer = SevenSegmentsPrinter([ssd_0, ssd_1])
        printer.show()
        self.assertEquals(sys.stdout.getvalue(),
            ' -    \n' +
            '| |  |\n' +
            '      \n' +
            '| |  |\n' +
            ' -    \n')

    def test_print_012(self):
        ssd_0 = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')])
        ssd_1 = SevenSegmentsDisplay(1, [(' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')])
        ssd_2 = SevenSegmentsDisplay(1, [(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' ')])
        printer = SevenSegmentsPrinter([ssd_0, ssd_1, ssd_2])
        printer.show()
        self.assertEquals(sys.stdout.getvalue(),
            ' -     - \n' +
            '| |  |  |\n' +
            '       - \n' +
            '| |  ||  \n' +
            ' -     - \n')


if __name__ == '__main__':
    unittest.main()