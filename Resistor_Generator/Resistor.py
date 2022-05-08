import string
import Rectangle


class Resistor:
    legLeftPosition = ()
    legRightPosition = ()
    codeBarPosition = []
    codeBarWidth = 0
    codeBarColor = []
    color = [
        (20, 20, 20),       # Black
        (110, 38, 14),      # Brown
        (204, 0, 0),        # Red
        (255, 128, 0),      # Orange
        (204, 204, 51),     # Yellow
        (0, 204, 80),       # Green
        (0, 0, 204),        # Blue
        (102, 0, 204),      # Violet
        (128, 128, 128),    # Grey
        (230, 230, 230),    # White
        (218, 165, 32),     # Gold
        (192, 192, 192)     # Silver
    ]


    def __init__(self, specification: tuple, bodyPosition: tuple, bodySize: tuple, bodyColor: tuple, legSize: tuple, legColor: tuple, codeBarCount: int,
            codeBarClearanceSide: int, codeBarClearance: int) -> None:

        self.specification = specification
        self.bodyPosition = bodyPosition
        self.bodySize = bodySize
        self.bodyColor = bodyColor
        self.legSize = legSize
        self.legColor = legColor
        self.codeBarCount = codeBarCount
        self.codeBarClearanceSide = codeBarClearanceSide
        self.codeBarClearance = codeBarClearance

        # The code bar with must be greather than 2 so work correctly
        if self.codeBarCount < 3:
            print("ERROR: Resistor code bar count too small:", self.codeBarCount)
            print("-> This number must be greather than 2 to work correctly")
            return

        self.CodeBarPositionCalculate()
        self.CodeBarColorCalculate()


    def CodeBarPositionCalculate(self) -> bool:
        # Calculate different resistor leg attributes
        self.legLeftPosition = (self.bodyPosition[0] - self.legSize[0], self.bodyPosition[1] + int(self.bodySize[1] / 2) - int(self.legSize[1] / 2))
        self.legRightPosition = (self.bodyPosition[0] + self.bodySize[0], self.legLeftPosition[1])

        # Determine the code with for each color bar depending which resistor
        # code type is selected
        self.codeBarWidth = self.bodySize[0] - (2 * self.codeBarClearanceSide)
        self.codeBarWidth = int((self.codeBarWidth - (self.codeBarCount * self.codeBarClearance)) / self.codeBarCount)

        # Check if the resistor bar code width is more than 0.
        if self.codeBarWidth <= 0:
            print("ERROR: Resistor code bar width too small:", self.codeBarWidth)
            print("-> Increase the resistor body or decrease the clearance")
            return False

        # Calculate resistor bar code positions
        self.codeBarPosition.append((self.bodyPosition[0] + self.codeBarClearanceSide, self.bodyPosition[1]))

        for counter in range(self.codeBarCount - 2):
            self.codeBarPosition.append((self.codeBarPosition[counter][0] + self.codeBarWidth + self.codeBarClearance, self.bodyPosition[1]))

        self.codeBarPosition.append((self.codeBarPosition[counter + 1][0] + self.codeBarWidth + 2 * self.codeBarClearance, self.bodyPosition[1]))
        return True


    def CodeBarColorCalculate(self) -> None:
        specificationValue = self.specification[0]
        specificationMultiplier = 0
        specificationTolerance = self.specification[1]

        # TODO: Add support for 0.1 and 0.01 multiplier. Throw a warning if the
        # multiplier was too small and can not be supported. But do not stop
        # script execution so there will be trailing black code bars
        # TODO: Throw a warning if the resistor value was being cropped down
        # because of precision reasons

        # Get multiplier value
        while specificationValue >= 10 ** (self.codeBarCount - 2):
            specificationValue = int(specificationValue / 10)
            specificationMultiplier += 1

        # Generate list with correct amount of code bar count
        for counter in range(self.codeBarCount):
            self.codeBarColor.append(0)

        # Add code bar colors
        for counter in range(self.codeBarCount - 3, -1, -1):
            self.codeBarColor[counter] = self.color[specificationValue % 10]
            specificationValue = int(specificationValue / 10)

        # Add multiplier bar color
        self.codeBarColor[self.codeBarCount - 2] = self.color[specificationMultiplier]

        # TODO: Correctly determine tolerance color

        # Add tolerance bar color
        self.codeBarColor[self.codeBarCount - 1] = self.color[10]


    def Draw(self, image: list, imageSize: tuple) -> None:
        # Draw each rectangle from back to front into the image
        Rectangle.Draw(image, imageSize, self.bodyPosition, self.bodySize, self.bodyColor)
        Rectangle.Draw(image, imageSize, self.legLeftPosition, self.legSize, self.legColor)
        Rectangle.Draw(image, imageSize, self.legRightPosition, self.legSize, self.legColor)

        for counter in range(self.codeBarPosition.__len__()):
            Rectangle.Draw(image, imageSize, self.codeBarPosition[counter], (self.codeBarWidth, self.bodySize[1]), self.codeBarColor[counter])
