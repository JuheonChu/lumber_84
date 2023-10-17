from GraphAndNode import*

def GraphifyI(file):
    '''Function that takes in an AST File and converts it to a Graph'''
    ASTGraph = Graph()
    lines = file.readlines()
    for line in lines:
        level = line.count('\t')+1 #find the level of a given line
        tempList = line.split(',')
        lineNum = tempList[-1].strip() #the last component of the list is the line number
        content = tempList[0].lstrip()
        ASTGraph.add_node(content, level, lineNum)

    ASTGraph.display() #to see if the code is working correctly

#Testing the code on a dummy AST        
with open('SchoolClassAST.txt', 'rt') as theFile:
    GraphifyI(theFile)