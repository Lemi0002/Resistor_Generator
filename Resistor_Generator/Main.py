import sys
import png
import Resistor
import ArgumentParser
import Parser


image = []
imageSize = (41, 9)

# Resistor Specification: Value in Ohm, tolerance in percentage
resistorSpecification = (12, 10)
resistorBodyPosition = (6, 1)
resistorBodySize = (29, 7)
resistorBodyColor = (100, 204, 180)
resistorLegSize = (5, 3)
resistorLegColor = (50, 50, 50)
resistorCodeBarCount = 5
resistorCodeBarClearanceSide = 2
resistorCodeBarClearance = 2
backgroundColor = (255, 255, 255)

parser = Parser.Parser("_RG_", "::", "_", None)
parser.stringParse("Hello_RG_::There::::You::_World")

# Parse all arguments and check if all flags have the correct amount of
# arguments
if ArgumentParser.parse(sys.argv) == False:
    quit()

resistor = Resistor.Resistor(resistorSpecification, resistorBodyPosition, resistorBodySize, resistorBodyColor, resistorLegSize, resistorLegColor,
    resistorCodeBarCount, resistorCodeBarClearanceSide, resistorCodeBarClearance)

# Generate image list
for counter in range(imageSize[0] * imageSize[1]):
    image.append(backgroundColor)

# Draw resistor to image
resistor.draw(image, imageSize)

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
