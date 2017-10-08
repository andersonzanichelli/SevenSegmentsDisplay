import unittest
from sevensegmentsdisplay import SevenSegmentsDisplay

class TestSevenSegmentsDisplayNumbers(unittest.TestCase):

    def test_A(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' ')])
        self.assertEqual(' ', self.ssd.topLeft())
        self.assertEqual('-', self.ssd.topCenter())
        self.assertEqual(' ', self.ssd.topRight())

        self.assertEqual('|', self.ssd.midTopLeft())
        self.assertEqual(' ', self.ssd.midTopCenter())
        self.assertEqual('|', self.ssd.midTopRight())

        self.assertEqual(' ', self.ssd.midLeft())
        self.assertEqual('-', self.ssd.midCenter())
        self.assertEqual(' ', self.ssd.midRight())

        self.assertEqual('|', self.ssd.midBottonLeft())
        self.assertEqual(' ', self.ssd.midBottonCenter())
        self.assertEqual('|', self.ssd.midBottonRight())

        self.assertEqual(' ', self.ssd.bottonLeft())
        self.assertEqual(' ', self.ssd.bottonCenter())
        self.assertEqual(' ', self.ssd.bottonRight())

    def test_B(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), ('|', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')])
        self.assertEqual(' ', self.ssd.topLeft())
        self.assertEqual('-', self.ssd.topCenter())
        self.assertEqual(' ', self.ssd.topRight())

        self.assertEqual('|', self.ssd.midTopLeft())
        self.assertEqual(' ', self.ssd.midTopCenter())
        self.assertEqual('|', self.ssd.midTopRight())

        self.assertEqual('|', self.ssd.midLeft())
        self.assertEqual('-', self.ssd.midCenter())
        self.assertEqual(' ', self.ssd.midRight())

        self.assertEqual('|', self.ssd.midBottonLeft())
        self.assertEqual(' ', self.ssd.midBottonCenter())
        self.assertEqual('|', self.ssd.midBottonRight())

        self.assertEqual(' ', self.ssd.bottonLeft())
        self.assertEqual('-', self.ssd.bottonCenter())
        self.assertEqual(' ', self.ssd.bottonRight())

    def test_zero(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')])
        self.assertEqual(' ', self.ssd.topLeft())
        self.assertEqual('-', self.ssd.topCenter())
        self.assertEqual(' ', self.ssd.topRight())

        self.assertEqual('|', self.ssd.midTopLeft())
        self.assertEqual(' ', self.ssd.midTopCenter())
        self.assertEqual('|', self.ssd.midTopRight())

        self.assertEqual(' ', self.ssd.midLeft())
        self.assertEqual(' ', self.ssd.midCenter())
        self.assertEqual(' ', self.ssd.midRight())

        self.assertEqual('|', self.ssd.midBottonLeft())
        self.assertEqual(' ', self.ssd.midBottonCenter())
        self.assertEqual('|', self.ssd.midBottonRight())

        self.assertEqual(' ', self.ssd.bottonLeft())
        self.assertEqual('-', self.ssd.bottonCenter())
        self.assertEqual(' ', self.ssd.bottonRight())

    def test_one(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')])
        self.assertEqual(' ', self.ssd.topLeft())
        self.assertEqual(' ', self.ssd.topCenter())
        self.assertEqual(' ', self.ssd.topRight())

        self.assertEqual(' ', self.ssd.midTopLeft())
        self.assertEqual(' ', self.ssd.midTopCenter())
        self.assertEqual('|', self.ssd.midTopRight())

        self.assertEqual(' ', self.ssd.midLeft())
        self.assertEqual(' ', self.ssd.midCenter())
        self.assertEqual(' ', self.ssd.midRight())

        self.assertEqual(' ', self.ssd.midBottonLeft())
        self.assertEqual(' ', self.ssd.midBottonCenter())
        self.assertEqual('|', self.ssd.midBottonRight())

        self.assertEqual(' ', self.ssd.bottonLeft())
        self.assertEqual(' ', self.ssd.bottonCenter())
        self.assertEqual(' ', self.ssd.bottonRight())

    def test_two(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' ')])
        self.assertEqual(' ', self.ssd.topLeft())
        self.assertEqual('-', self.ssd.topCenter())
        self.assertEqual(' ', self.ssd.topRight())

        self.assertEqual(' ', self.ssd.midTopLeft())
        self.assertEqual(' ', self.ssd.midTopCenter())
        self.assertEqual('|', self.ssd.midTopRight())

        self.assertEqual(' ', self.ssd.midLeft())
        self.assertEqual('-', self.ssd.midCenter())
        self.assertEqual(' ', self.ssd.midRight())

        self.assertEqual('|', self.ssd.midBottonLeft())
        self.assertEqual(' ', self.ssd.midBottonCenter())
        self.assertEqual(' ', self.ssd.midBottonRight())

        self.assertEqual(' ', self.ssd.bottonLeft())
        self.assertEqual('-', self.ssd.bottonCenter())
        self.assertEqual(' ', self.ssd.bottonRight())

    
if __name__ == '__main__':
    unittest.main()