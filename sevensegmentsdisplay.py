class SevenSegmentsDisplay:

    def __init__(self, size, *segments):
        self.size = size
        self.segments = segments

    def topLeft(self):
        return self.segments[0][0][0]

    def topCenter(self):
        return self.segments[0][0][1]

    def topRight(self):
        return self.segments[0][0][2]

    def midTopLeft(self):
        return self.segments[0][1][0]

    def midTopCenter(self):
        return self.segments[0][1][1]

    def midTopRight(self):
        return self.segments[0][1][2]

    def midLeft(self):
        return self.segments[0][2][0]

    def midCenter(self):
        return self.segments[0][2][1]

    def midRight(self):
        return self.segments[0][2][2]

    def midBottonLeft(self):
        return self.segments[0][3][0]

    def midBottonCenter(self):
        return self.segments[0][3][1]

    def midBottonRight(self):
        return self.segments[0][3][2]

    def bottonLeft(self):
        return self.segments[0][4][0]

    def bottonCenter(self):
        return self.segments[0][4][1]

    def bottonRight(self):
        return self.segments[0][4][2]