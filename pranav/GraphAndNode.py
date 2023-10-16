class Node:
    def __init__(self, initContent, initLevel, initLineNumber, initParent):
        self.content = initContent
        self.level = initLevel
        self.lineNumber = initLineNumber
        self.parent = initParent

    def getContent(self):
        return self.content
    
    def getLevel(self):
        return self.initLevel
    
    def getLineNumber(self):
        return self.lineNumber
    
    def getParent(self):
        return self.parent
    
    def setContent(self, newContent):
        self.content = newContent

    def setParent(self, newParent):
        self.parent = newParent

