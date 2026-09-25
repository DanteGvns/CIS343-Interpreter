

class Token:
    def __init__(self, lineNumber, type):
        self.lineNumber = lineNumber
        self.type = type

    def getLineNumber(self):
        return f"This is at line: {self.lineNumber}."

    def getType(self):
        return f"{self.type}"   

    def showError(error):
        print(error)

class Number(Token):
    def __init__(self, lineNumber, value):
        self.type = "Number"
        super().__init__(lineNumber, self.type)
        self.value = value
        

class Word(Token):
    def __init__(self, lineNumber, value):
        self.type = "Word"
        super().__init__(lineNumber, self.type)
        self.value = value    

class Symbol(Token):
    def __init__(self, lineNumber, value):
        self.type = "Symbol"
        super().__init__(lineNumber, self.type)
        self.value = value 