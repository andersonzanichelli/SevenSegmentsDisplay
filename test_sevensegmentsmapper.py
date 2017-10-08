import unittest
from sevensegmentsmapper import SevenSegmentsMapper

class TestSevenSegmentsMapper(unittest.TestCase):

    def test_zero(self):
        ssm = SevenSegmentsMapper(0)
        self.assertEqual([(' ', '-', ' '), ('|', ' ', '|'), (' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

    def test_one(self):
        ssm = SevenSegmentsMapper(1)
        self.assertEqual([(' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')], ssm.mapped())

    def test_two(self):
        ssm = SevenSegmentsMapper(2)
        self.assertEqual([(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' ')], ssm.mapped())

    def test_three(self):
        ssm = SevenSegmentsMapper(3)
        self.assertEqual([(' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

    def test_four(self):
        ssm = SevenSegmentsMapper(4)
        self.assertEqual([(' ', ' ', ' '), ('|', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', ' ', ' ')], ssm.mapped())

    def test_five(self):
        ssm = SevenSegmentsMapper(5)
        self.assertEqual([(' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

    def test_six(self):
        ssm = SevenSegmentsMapper(6)
        self.assertEqual([(' ', '-', ' '), ('|', ' ', ' '), (' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

    def test_seven(self):
        ssm = SevenSegmentsMapper(7)
        self.assertEqual([(' ', '-', ' '), (' ', ' ', '|'), (' ', ' ', ' '), (' ', ' ', '|'), (' ', ' ', ' ')], ssm.mapped())

    def test_eight(self):
        ssm = SevenSegmentsMapper(8)
        self.assertEqual([(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

    def test_nine(self):
        ssm = SevenSegmentsMapper(9)
        self.assertEqual([(' ', '-', ' '), ('|', ' ', '|'), (' ', '-', ' '), (' ', ' ', '|'), (' ', '-', ' ')], ssm.mapped())

if __name__ == '__main__':
    unittest.main()