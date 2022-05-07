from turtle import pos
from typing import Tuple
import png

def RectangleDraw(image, imageSize, rectanglePosition, rectangleSize, rectangleColor):
    for counterY in range(rectanglePosition[1], rectanglePosition[1] + rectangleSize[1]):
        for counterX in range(rectanglePosition[0], rectanglePosition[0] + rectangleSize[0]):
            if (counterX >= 0 and counterX < imageSize[0]) and (counterY >= 0 and counterY < imageSize[1]):
                image[counterX + counterY * imageSize[0]] = rectangleColor

image = []
imageSize = (52, 9)

# Resistor Specification: Value in Ohm, tolerance in percentage
resistorSpecification = (1200, 5)

resistorBodyPosition = (6, 1)
resistorBodySize = (40, 7)
resistorBodyColor = (100, 204, 180)
resistorLegSize = (5, 3)
resistorLegColor = (50, 50, 50)
resistorBackgroundColor = (255, 255, 255)
resistorCodeBarCount = 12
resistorCodeBarBodyClearance = 2
resistorCodeBarClearance = 1
resistorCodeBarPosition = []
resistorCodeBarColor = [
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

# Calculate different resistor leg attributes
resistorLegLeftPosition = (resistorBodyPosition[0] - resistorLegSize[0], resistorBodyPosition[1] + int(resistorBodySize[1] / 2) - int(resistorLegSize[1] / 2))
resistorLegRightPosition = (resistorBodyPosition[0] + resistorBodySize[0], resistorLegLeftPosition[1])

# Determine the code with for each color bar depending which resistor code type is selected
resistorCodeBarWidth = resistorBodySize[0] - (2 * resistorCodeBarBodyClearance)
resistorCodeBarWidth = int((resistorCodeBarWidth - (resistorCodeBarCount * resistorCodeBarClearance)) / resistorCodeBarCount)

# Check if the resistor bar code width is more than 0
if resistorCodeBarWidth <= 0:
    print("ERROR: Resistor code bar width too small:", resistorCodeBarWidth)
    quit()

# Calculate resistor bar code positions
resistorCodeBarPosition.append((resistorBodyPosition[0] + resistorCodeBarBodyClearance, resistorBodyPosition[1]))

for counter in range(resistorCodeBarCount - 2):
    resistorCodeBarPosition.append((resistorCodeBarPosition[counter][0] + resistorCodeBarWidth + resistorCodeBarClearance, resistorBodyPosition[1]))

resistorCodeBarPosition.append((resistorCodeBarPosition[counter + 1][0] + resistorCodeBarWidth + 2 * resistorCodeBarClearance, resistorBodyPosition[1]))

# Generate image list
for counter in range(imageSize[0] * imageSize[1]):
    image.append(resistorBackgroundColor)

# Draw each rectangle from back to front into the image
RectangleDraw(image, imageSize, resistorBodyPosition, resistorBodySize, resistorBodyColor)
RectangleDraw(image, imageSize, resistorLegLeftPosition, resistorLegSize, resistorLegColor)
RectangleDraw(image, imageSize, resistorLegRightPosition, resistorLegSize, resistorLegColor)

for counter in range(resistorCodeBarCount):
    RectangleDraw(image, imageSize, resistorCodeBarPosition[counter], (resistorCodeBarWidth, resistorBodySize[1]), resistorCodeBarColor[counter])

# Generate png file
with open('Resistor.png', 'wb') as file:
    imagePng = []
    for counterY in range(imageSize[1]):
        row =  ()

        for counterX in range(imageSize[0]):
            row += image[counterX + counterY * imageSize[0]]

        imagePng.append(row)

    pngWriter = png.Writer(imageSize[0], imageSize[1], greyscale=False)
    pngWriter.write(file, imagePng)

print("INFO: Program successfully executed")
