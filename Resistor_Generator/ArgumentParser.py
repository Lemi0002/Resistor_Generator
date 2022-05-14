# The first entry of each type is its specific flag number. The second one is
# the amount of arguments which must be appended to this flag
argumentFlagTypeNone = (0, 0)
argumentFlagTypeInput = (1, 1)
argumentFlagTypeHelp = (2, 0)
argumentFlagTypeVersion = (3, 0)
argumentParsed = []
argumentFlags = [
    ("-i", argumentFlagTypeInput),
    ("--input", argumentFlagTypeInput),
    ("--help", argumentFlagTypeHelp),
    ("--version", argumentFlagTypeVersion)
]


def parse(arguments: list) -> None:
    returnValue = True

    # Determine the specific flag number of each flag
    for counterArguments in range(arguments.__len__()):
        for counterFlag in range(argumentFlags.__len__()):
            if argumentFlags[counterFlag][0] == arguments[counterArguments]:
                argumentParsed.append(argumentFlags[counterFlag][1])
                break
            elif counterFlag == argumentFlags.__len__() - 1:
                argumentParsed.append(argumentFlagTypeNone)

    # Iterate through the created list and check if the specific amount of
    # arguments follow each flag
    flagActive = argumentFlagTypeNone
    flagActiveArgumentCount = flagActive[1]
    flagActiveIndex = 0

    for counter in range(argumentParsed.__len__()):
        if argumentParsed[counter][0] > argumentFlagTypeNone[0] and flagActiveArgumentCount > 0:
            print("ERROR: Flag", arguments[flagActiveIndex], "at index", flagActiveIndex, "has", flagActiveArgumentCount, "missing arguments")
            print("-> Use correct flag and argument format")
            returnValue = False

            flagActive = argumentParsed[counter]
            flagActiveArgumentCount = flagActive[1]
            flagActiveIndex = counter
        elif flagActiveArgumentCount > 0:
            flagActiveArgumentCount -= 1
        else:
            flagActive = argumentParsed[counter]
            flagActiveArgumentCount = flagActive[1]
            flagActiveIndex = counter

    # Check if the last flag has enough arguments
    if flagActiveArgumentCount > 0:
        print("ERROR: Flag", arguments[flagActiveIndex], "at index", flagActiveIndex, "has", flagActiveArgumentCount, "missing arguments")
        print("-> Use correct flag and argument format")
        returnValue = False

    # TODO: Detect redundant arguments and trow an error

    return returnValue
