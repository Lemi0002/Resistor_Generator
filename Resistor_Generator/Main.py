import png
import Resistor

image = []
imageSize = (52, 9)

# Resistor Specification: Value in Ohm, tolerance in percentage
resistorSpecification = (1200, 5)

resistorBodyPosition = (6, 1)
resistorBodySize = (40, 7)
resistorBodyColor = (100, 204, 180)
resistorLegSize = (5, 3)
resistorLegColor = (50, 50, 50)
backgroundColor = (255, 255, 255)
resistorCodeBarCount = 12
resistorCodeBarBodyClearance = 2
resistorCodeBarClearance = 1

resistor = Resistor.Resistor(resistorSpecification, resistorBodyPosition, resistorBodySize, resistorBodyColor, resistorLegSize, resistorLegColor, resistorCodeBarCount,
    resistorCodeBarBodyClearance, resistorCodeBarClearance)

# Generate image list
for counter in range(imageSize[0] * imageSize[1]):
    image.append(backgroundColor)

# Draw resistor to image
resistor.Draw(image, imageSize)

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