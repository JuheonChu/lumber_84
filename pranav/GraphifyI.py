def GraphifyI(file):
    '''Function that takes in an AST File and converts it to a Graph'''
    graphList = []
    lines = file.readLines()
    for line in lines:
        numLeadingWhitespaces = len(line) - len(line.lstrip()) #obtain the number of leaing whitespaces
        level = numLeadingWhitespaces/4 + 1 #find the level of a given line
        tempList = line.split(',')
        lineNum = tempList[-1] #the last component of the list is the line number
        content = tempList[0].lstrip()
        #Create an edge object
        #add edge object to graph
