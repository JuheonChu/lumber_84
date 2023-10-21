#!/usr/bin/env python
'''GraphAndNode.py: This python file defines a Node and Graph Class required to process the contents of an Abstract Syntax Tree'''
'''Informally, an AST is the skeleton of any given computer program; that is, it represents the most important syntax of a 
program. Formally, an AST is a data structure that comprises the parsed contents of a given program - taking into account the 
syntax and the semantics of the programming language, including the hierarchy of the program structure (Classes, methods, loops, conditionals)
as well as sequence of instructions. In particular, this Graph data structure was developed to manage the contents of the ASTs
generated for the CBasic 86 (CB86) code of 84 Lumber'''
__author__  = "Pranav Mishra"
__version__ = "1.0"
__maintainer__ = "Pranav Mishra"
__email__ = "mishrap@dickinson.edu"


class Node:
    '''This class defines a node pertaining to a given Abstract Syntax Tree line'''
    def __init__(self, initContent, initLevel, initLineNumber, initParent):
        '''Each node object consists of some content it represents, the level of the node, the corresponding line number of the code, and a reference 
        to the parent node'''
        self.content = initContent
        self.level = initLevel
        self.lineNumber = initLineNumber
        self.parent = initParent
        self.children = []

    def getContent(self):
        '''get the content associated with a given node'''
        return self.content
    
    def getLevel(self):
        '''get the level associated with a given node'''
        return self.level
    
    def getLineNumber(self):
        '''get the line number associated with a given node'''
        return self.lineNumber
    
    def getParent(self):
        '''get the parent of a given node'''
        return self.parent
    
    def getChildren(self):
        '''get all the children '''
        return self.children
    
    def setContent(self, newContent):
        '''set the content associated with a particular node'''
        self.content = newContent

    def setParent(self, newParent):
        '''set the parent associated with a particular node'''
        self.parent = newParent

    def addChild(self, newChild):
        '''add a new child associated with a particular node'''
        self.children.append(newChild)
        newChild.setParent(self)

    def isRoot(self):
        '''return true if a given node is a root, or false otherwise'''
        return self.parent == None

class Graph:
    def __init__(self):
        '''By definition, a graph is a collection of root nodes that have children that are represented in lists, whose children
        too are represented in lists, and so on and so forth'''
        self.roots = []

    def getLastRoot(self):
        '''returns the last root object'''
        return self.roots[-1]
    
    def getLastChildAtLevel(self, level):
        '''returns the last child at a given level'''
        if level == 1:
            lastChildAtTheLevel = self.getLastRoot()
        else:
            lastRoot = self.getLastRoot()
            lastChild = lastRoot
            for i in range(1, level):
                lastChildOfLastNode = lastChild.getChildren()[-1]
                lastChild = lastChildOfLastNode
            
            lastChildAtTheLevel = lastChild

        return lastChildAtTheLevel
        
    def add_node(self, content, level, lineNumber):
        '''Add a node to the graph in breadth first order'''
        if level == 1:
            newNode = Node(content, level, lineNumber, None)
            self.roots.append(newNode)

        else:
            lastChildAtPrecedingLevel = self.getLastChildAtLevel(level-1)
            newNode = Node(content, level, lineNumber, lastChildAtPrecedingLevel)
            lastChildAtPrecedingLevel.addChild(newNode)

    def display(self):
        '''Display the nodes in the graph'''
        for root in self.roots:
            stack = [(root, 0)]

            while stack:
                current_node, current_level = stack.pop()

                print("  " * current_level + f"Level {current_node.getLevel()}: {current_node.getContent()} (Line {current_node.getLineNumber()})")

                for child in reversed(current_node.getChildren()):
                    stack.append((child, current_level + 1))

if __name__ == "__main__":
    # Example usage:
    graph = Graph()
    graph.add_node("Root 1", 1, 1)
    graph.add_node("Child 1", 2, 2)
    graph.add_node("Child 2", 2, 3)
    graph.add_node("Child 3", 2, 4)
    graph.add_node("Grandchild 1", 3, 5)
    graph.add_node("Root 2", 1, 6)
    graph.add_node("Child 4", 2, 7)
    graph.add_node("Root 3", 1, 8)
    graph.add_node("Root 4", 1, 9)

    # Display the hierarchy
    graph.display()  # Display hierarchy starting from all root nodes