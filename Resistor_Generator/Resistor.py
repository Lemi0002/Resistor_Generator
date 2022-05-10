import Rectangle


class Resistor:
    specificationMultiplierMin = -2
    specificationMultiplierMax = 9
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
        (192, 192, 192),    # Silver
        (218, 165, 32)      # Gold
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

        self.__CodeBarPositionCalculate()
        self.__CodeBarColorCalculate()


    def Draw(self, image: list, imageSize: tuple) -> None:
        if imageSize.__len__() < 2:
            print("ERROR: Not correct tuple format")
            print("-> Inserted size and position tuples must be two dimensional")
            return False

        # Draw each rectangle from back to front into the image
        Rectangle.Draw(image, imageSize, self.bodyPosition, self.bodySize, self.bodyColor)
        Rectangle.Draw(image, imageSize, self.legLeftPosition, self.legSize, self.legColor)
        Rectangle.Draw(image, imageSize, self.legRightPosition, self.legSize, self.legColor)

        for counter in range(self.codeBarPosition.__len__()):
            Rectangle.Draw(image, imageSize, self.codeBarPosition[counter], (self.codeBarWidth, self.bodySize[1]), self.codeBarColor[counter])

        return True


    def __CodeBarPositionCalculate(self) -> bool:
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


    def __CodeBarColorCalculate(self) -> None:
        specificationValue = self.specification[0]
        specificationMultiplier = 0

        # Get negative multiplier exponent
        while specificationValue < 10 ** (self.codeBarCount - 3):
            if specificationMultiplier > self.specificationMultiplierMin:
                specificationValue = specificationValue * 10
                specificationMultiplier -= 1
            else:
                print("WARNING: Multiplier would be smaller than:", self.specificationMultiplierMin)
                print("-> Insert a bigger resistor value or reduce the code bar count")
                break

        # Cast to a full integer. Only needed when the value has a negative
        # exponent
        specificationValue = int(specificationValue)

        # Get positive multiplier exponent
        while specificationValue >= 10 ** (self.codeBarCount - 2):
            if specificationMultiplier < self.specificationMultiplierMax:
                specificationValue = int(specificationValue / 10)
                specificationMultiplier += 1
            else:
                print("WARNING: Multiplier would be bigger than:", self.specificationMultiplierMax)
                print("-> Insert a smaller resistor value or increase the code bar count")
                break

        # TODO: Boundary check multiplier

        # Throw a warning if the resistor value was cropped
        specificationValueCropped = specificationValue * (10 ** specificationMultiplier)

        if self.specification[0] > specificationValueCropped:
            print("WARNING: Resistor value was cropped from:", self.specification[0], "to:", specificationValueCropped)
            print("-> Insert a resistor value with the correct amount of digits or increase the code bar count")

        # Generate list with correct amount of code bar count
        for counter in range(self.codeBarCount):
            self.codeBarColor.append(0)

        # Add code bar colors
        for counter in range(self.codeBarCount - 3, -1, -1):
            self.codeBarColor[counter] = self.color[specificationValue % 10]
            specificationValue = int(specificationValue / 10)

        # Add multiplier bar color
        if specificationMultiplier >= 0:
            self.codeBarColor[self.codeBarCount - 2] = self.color[specificationMultiplier]
        else:
            self.codeBarColor[self.codeBarCount - 2] = self.color[12 + specificationMultiplier]

        # TODO: Correctly determine tolerance color

        # Add tolerance bar color
        self.codeBarColor[self.codeBarCount - 1] = self.color[11]
