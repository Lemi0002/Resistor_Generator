import sys
import png
import Resistor
import Parser
import Auxillary


inputPath = ""
inputFileList = []
outputPath = ""
imageSize = (41, 9)
resistorBodyPosition = (6, 1)
resistorBodySize = (29, 7)
resistorBodyColor = (100, 204, 180)
resistorLegSize = (5, 3)
resistorLegColor = (50, 50, 50)
resistorCodeBarCount = 5
resistorCodeBarClearanceSide = 2
resistorCodeBarClearance = 2
backgroundColor = (255, 255, 255)
colorMin = 0
colorMax = 255
codeBarCountMin = 4
codeBarCountMax = 5


def consoleCallbackInput(parameter: list) -> None:
    inputFileList.append(parameter[0])


def consoleCallbackHelp(parameter: list) -> None:
    print("Available console arguments:")

    for counter in range(consoleArgumentFlags.__len__()):
        print("   ", consoleArgumentFlags[counter][0])

    print("")
    print("Available file arguments:")

    for counter in range(fileArgumentFlags.__len__()):
        print("   ",fileArgumentFlags[counter][0])

    print("")


def consoleCallbackVersion(parameter: list) -> None:
    # TODO: Use correct version
    print("Version: 1.0.0")


def fileCallbackSpecification(parameter: list) -> None:
    try:
        image = []
        resistorSpecification = (Auxillary.toUnsigned(int(parameter[0])), Auxillary.toUnsigned(int(parameter[1])))
        resistor = Resistor.Resistor(resistorSpecification, resistorBodyPosition, resistorBodySize, resistorBodyColor, resistorLegSize, resistorLegColor,
            resistorCodeBarCount, resistorCodeBarClearanceSide, resistorCodeBarClearance)

        for counter in range(imageSize[0] * imageSize[1]):
            image.append(backgroundColor)

        # Draw resistor to image
        resistor.draw(image, imageSize)

        # TODO: Generate correct output path
        imagePngName = "Resistor_" + str(resistorSpecification[0]) + "_" + str(resistorSpecification[1])
        imagePngPath = outputPath + imagePngName + ".png"

        # Generate png file
        try:
            imagePng = open(imagePngPath, "wb")

            imagePngList = []
            for counterY in range(imageSize[1]):
                row =  ()

                for counterX in range(imageSize[0]):
                    row += image[counterX + counterY * imageSize[0]]

                imagePngList.append(row)

            pngWriter = png.Writer(imageSize[0], imageSize[1], greyscale=False)
            pngWriter.write(imagePng, imagePngList)

            imagePng.close()
        except:
            print("ERROR: Could not open file:", imagePngPath)
            print("-> Check if the selected file exists")
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackOutputPath(parameter: list) -> None:
    global outputPath

    outputPath = parameter[0]


def fileCallbackImageSize(parameter: list) -> None:
    global imageSize

    try:
        imageSize = (Auxillary.toUnsigned(int(parameter[0])), Auxillary.toUnsigned(int(parameter[1])))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackBodyPosition(parameter: list) -> None:
    global resistorBodyPosition

    try:
        resistorBodyPosition = (Auxillary.toUnsigned(int(parameter[0])), Auxillary.toUnsigned(int(parameter[1])))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackBodySize(parameter: list) -> None:
    global resistorBodySize

    try:
        resistorBodySize = (Auxillary.toUnsigned(int(parameter[0])), Auxillary.toUnsigned(int(parameter[1])))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackBodyColor(parameter: list) -> None:
    global resistorBodyColor

    try:
        color = (int(parameter[0]), int(parameter[1]), int(parameter[2]))
        resistorBodyColor = (Auxillary.rangeCheck(color[0], colorMin, colorMax), Auxillary.rangeCheck(color[1], colorMin, colorMax), Auxillary.rangeCheck(color[2], colorMin, colorMax))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackLegSize(parameter: list) -> None:
    global resistorLegSize

    try:
        resistorLegSize = (Auxillary.toUnsigned(int(parameter[0])), Auxillary.toUnsigned(int(parameter[1])))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackLegColor(parameter: list) -> None:
    global resistorLegColor

    try:
        color = (int(parameter[0]), int(parameter[1]), int(parameter[2]))
        resistorLegColor = (Auxillary.rangeCheck(color[0], colorMin, colorMax), Auxillary.rangeCheck(color[1], colorMin, colorMax), Auxillary.rangeCheck(color[2], colorMin, colorMax))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackCodeBarCount(parameter: list) -> None:
    global resistorCodeBarCount

    try:
        resistorCodeBarCount = Auxillary.rangeCheck(int(parameter[0]), codeBarCountMin, codeBarCountMax)
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackCodeBarClearanceSide(parameter: list) -> None:
    global resistorCodeBarClearanceSide

    try:
        resistorCodeBarClearanceSide = Auxillary.toUnsigned(int(parameter[0]))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackCodeBarClearance(parameter: list) -> None:
    global resistorCodeBarClearance

    try:
        resistorCodeBarClearance = Auxillary.toUnsigned(int(parameter[0]))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


def fileCallbackBackgroundColor(parameter: list) -> None:
    global backgroundColor

    try:
        color = (int(parameter[0]), int(parameter[1]), int(parameter[2]))
        backgroundColor = (Auxillary.rangeCheck(color[0], colorMin, colorMax), Auxillary.rangeCheck(color[1], colorMin, colorMax), Auxillary.rangeCheck(color[2], colorMin, colorMax))
    except:
        print("ERROR: Parameter is not an int:", parameter)
        print("-> Change parameter format")


consoleArgumentFlags = [
    ("-i", 1, consoleCallbackInput),
    ("--input", 1, consoleCallbackInput),
    ("--help", 0, consoleCallbackHelp),
    ("--version", 0, consoleCallbackVersion)
]
fileArgumentFlags = [
    ("Specification", 2, fileCallbackSpecification),
    ("OutputPath", 1, fileCallbackOutputPath),
    ("ImageSize", 2, fileCallbackImageSize),
    ("BodyPosition", 2, fileCallbackBodyPosition),
    ("BodySize", 2, fileCallbackBodySize),
    ("BodyColor", 3, fileCallbackBodyColor),
    ("LegSize", 2, fileCallbackLegSize),
    ("LegColor", 3, fileCallbackLegColor),
    ("CodeBarCount", 1, fileCallbackCodeBarCount),
    ("CodeBarClearanceSide", 1, fileCallbackCodeBarClearanceSide),
    ("CodeBarClearance", 1, fileCallbackCodeBarClearance),
    ("BackgroundColor", 3, fileCallbackBackgroundColor)
]

consoleParser = Parser.Parser("", " ", "", consoleArgumentFlags, True)
fileParser = Parser.Parser("_RG_", ";", "_", fileArgumentFlags, False)

# Execute command line commands or quit the application when something went
# wrong
if consoleParser.argumentsParse(sys.argv[1:]) == False:
    quit()

# Iterate through all input files
for counter in range(inputFileList.__len__()):
    try:
        inputFile = open(inputFileList[counter], "r")
        inputFileLines = inputFile.readlines()

        for counterLine in range(inputFileLines.__len__()):
            fileParser.stringParse(inputFileLines[counterLine], False)

        inputFile.close()
    except:
        print("ERROR: Could not open file:", inputFileList[counter])
        print("-> Check if the selected file exists")

print("INFO: Program successfully executed")
