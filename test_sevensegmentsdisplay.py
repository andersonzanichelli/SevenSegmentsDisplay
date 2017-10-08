import unittest
from sevensegmentsdisplay import SevenSegmentsDisplay

class TestSevenSegmentsDisplay(unittest.TestCase):

    def setUp(self):
        self.ssd = SevenSegmentsDisplay(1, [(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')])

    def test_topLeft(self):
        self.assertEqual(' ', self.ssd.topLeft())

    def test_topCenter(self):
        self.assertEqual('-', self.ssd.topCenter())

    def test_topRight(self):
        self.assertEqual(' ', self.ssd.topRight())

    def test_midTopLeft(self):
        self.assertEqual('|', self.ssd.midTopLeft())

    def test_midTopCenter(self):
        self.assertEqual(' ', self.ssd.midTopCenter())

    def test_midTopRight(self):
        self.assertEqual('|', self.ssd.midTopRight())

    def test_midLeft(self):
        self.assertEqual(' ', self.ssd.midLeft())

    def test_midCenter(self):
        self.assertEqual('-', self.ssd.midCenter())

    def test_midRight(self):
        self.assertEqual(' ', self.ssd.midRight())

    def test_midBottonLeft(self):
        self.assertEqual('|', self.ssd.midBottonLeft())

    def test_midBottonCenter(self):
        self.assertEqual(' ', self.ssd.midBottonCenter())

    def test_midBottonRight(self):
        self.assertEqual('|', self.ssd.midBottonRight())

    def test_bottonLeft(self):
        self.assertEqual(' ', self.ssd.bottonLeft())

    def test_bottonCenter(self):
        self.assertEqual('-', self.ssd.bottonCenter())

    def test_bottonRight(self):
        self.assertEqual(' ', self.ssd.bottonRight())

if __name__ == '__main__':
    unittest.main()