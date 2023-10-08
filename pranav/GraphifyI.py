def GraphifyI(file):
    '''Function that takes in an AST File and converts it to a Graph'''
    lines = file.readLines()
    for line in lines:
        numLeadingWhitespaces = len(line) - len(line.lstrip())
        level = numLeadingWhitespaces/4 + 1
        tempList = line.split(',')
        lineNum = tempList[-1]
        content = line[numLeadingWhitespaces+1:len(line)-2]
        #Create an edge object
        #add edge object to graph
