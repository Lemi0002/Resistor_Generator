from ast import Tuple


class Parser:
    stringStart = ""
    stringDelimiter = ""
    stringEnd = ""
    argumentFlags = []


    def __init__(self, stringStart: str = "", stringDelimiter: str = "", stringEnd: str = "", argumentFlags: list = []) -> None:
        self.stringStart = stringStart
        self.stringDelimiter = stringDelimiter
        self.stringEnd = stringEnd
        self.argumentFlags = argumentFlags


    def stringParse(self, string: str) -> bool:
        returnValue, arguments = self.__stringSplit(string)

        if returnValue == False:
            return False

        return self.argumentsParse(arguments)


    def argumentsParse(self, arguments: list) -> bool:
        returnValue = True
        argumentParsed = []
        argumentFlagNone = (None, 0, None)

        # Determine if the arguments are flags or not
        for counterArguments in range(arguments.__len__()):
            for counterFlag in range(self.argumentFlags.__len__()):
                if self.argumentFlags[counterFlag][0] == arguments[counterArguments]:
                    argumentParsed.append(self.argumentFlags[counterFlag])
                    break
                elif counterFlag == self.argumentFlags.__len__() - 1:
                    argumentParsed.append(argumentFlagNone)

        # Iterate through the created list and check if the specific amount of
        # arguments follow each flag. Set the callback to None to indicated that
        # there were not enough arguments for this specific flag and therefore,
        # the callback will not be called
        flagActive = argumentFlagNone
        flagActiveArgumentCount = flagActive[1]
        flagActiveIndex = 0

        for counter in range(argumentParsed.__len__()):
            if argumentParsed[counter][0] != argumentFlagNone[0] and flagActiveArgumentCount > 0:
                print("ERROR: Flag", arguments[flagActiveIndex], "at index", flagActiveIndex, "has", flagActiveArgumentCount, "missing arguments")
                print("-> Use correct flag and argument format")
                returnValue = False
                argumentParsed[flagActiveIndex] = flagActive[:2] + (None,)

                flagActive = argumentParsed[counter]
                flagActiveArgumentCount = flagActive[1]
                flagActiveIndex = counter
            elif flagActiveArgumentCount > 0:
                flagActiveArgumentCount -= 1
            else:
                flagActive = argumentParsed[counter]
                flagActiveArgumentCount = flagActive[1]
                flagActiveIndex = counter

            if argumentParsed[flagActiveIndex][0] == argumentFlagNone[0]:
                print("ERROR: Argument", arguments[flagActiveIndex], "at index", flagActiveIndex, "is redundant")
                print("-> Remove argument")
                returnValue = False

        # Check if the last flag has enough arguments. If not, set its callback
        # to None
        if flagActiveArgumentCount > 0:
            print("ERROR: Flag", arguments[flagActiveIndex], "at index", flagActiveIndex, "has", flagActiveArgumentCount, "missing arguments")
            print("-> Use correct flag and argument format")
            returnValue = False
            argumentParsed[flagActiveIndex] = flagActive[:2] + (None,)

        return returnValue


    def __stringSplit(self, string: str) -> Tuple(bool, list):
        indexStart = 0
        indexEnd = string.__len__()
        arguments = []

        # Get the first start string index
        if self.stringStart != "":
            indexStart = string.find(self.stringStart)

            if indexStart < 0:
                print("Error: Start string not found:", self.stringStart)
                print("-> Use different input string")
                return False, []

        # Get the first end string index after the start string
        if self.stringEnd != "":
            indexEnd = string.find(self.stringEnd, indexStart + self.stringStart.__len__())

            if indexEnd < 0:
                print("Error: End string not found:", self.stringEnd)
                print("-> Use different input string")
                return False, []

        # Get every argument between the start and end string
        if self.stringDelimiter != "":
            arguments = string[indexStart + self.stringStart.__len__() : indexEnd].split(self.stringDelimiter)
        else:
            arguments.append(string[indexStart + self.stringStart.__len__() : indexEnd])

        return True, arguments
