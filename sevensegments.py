from sevensegmentsmapper import SevenSegmentsMapper
from sevensegmentsdisplay import SevenSegmentsDisplay
from sevensegmentsprinter import SevenSegmentsPrinter

class SevenSegments:

    def run(self):
        print 'The 7 segments display.\n'
        self.size = input('Enter the size of the display: ')
        inputNumbers = input('Enter the numbers that you want display (comma separated: 1,2,3): ')

        if isinstance(inputNumbers, int):
            self.numbers = [inputNumbers]
        else:
            self.numbers = [int(c) for c in inputNumbers]

        mapped = []
        for number in self.numbers:
            mapped.append(SevenSegmentsMapper(number))

        displays = []
        for m in mapped:
            displays.append(SevenSegmentsDisplay(self.size, m.mapped()))

        printer = SevenSegmentsPrinter(displays)
        printer.show()

if __name__ == '__main__':
    app = SevenSegments()
    app.run()