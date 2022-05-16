class Parser:
    stringStart = ""
    stringDelimiter = ""
    stringEnd = ""
    arguments = []


    def __init__(self, stringStart: str, stringDelimiter: str, stringEnd: str, argumentFlags: list) -> None:
        self.stringStart = stringStart
        self.stringDelimiter = stringDelimiter
        self.stringEnd = stringEnd
        self.argumentFlags = argumentFlags


    def stringParse(self, string: str) -> bool:
        if self.__stringSplit(string) == False:
            return False

        return self.argumentsParse(self.arguments)


    def argumentsParse(self, arguments: list) -> bool:
        return True


    def __stringSplit(self, string: str) -> bool:
        indexStart = 0
        indexEnd = string.__len__()
        self.arguments.clear()

        # Get the first start string index
        if self.stringStart != "":
            indexStart = string.find(self.stringStart)

            if indexStart < 0:
                print("Error: Start string not found:", self.stringStart)
                print("-> Use different input string")
                return False

        # Get the first end string index after the start string
        if self.stringEnd != "":
            indexEnd = string.find(self.stringEnd, indexStart + self.stringStart.__len__())

            if indexEnd < 0:
                print("Error: End string not found:", self.stringEnd)
                print("-> Use different input string")
                return False

        # Get every argument between the start and end string
        if self.stringDelimiter != "":
            self.arguments = string[indexStart + self.stringStart.__len__() : indexEnd].split(self.stringDelimiter)
        else:
            self.arguments.append(string[indexStart + self.stringStart.__len__() : indexEnd])

        return True
