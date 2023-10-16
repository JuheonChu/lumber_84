class Node:
    def __init__(self, initContent, initLevel, initLineNumber, initParent):
        self.content = initContent
        self.level = initLevel
        self.lineNumber = initLineNumber
        self.parent = initParent
        self.children = []

    def getContent(self):
        return self.content
    
    def getLevel(self):
        return self.level
    
    def getLineNumber(self):
        return self.lineNumber
    
    def getParent(self):
        return self.parent
    
    def setContent(self, newContent):
        self.content = newContent

    def setParent(self, newParent):
        self.parent = newParent

class Graph:
    def __init__(self):
        self.root = None
        self.levels = {}

    def add_node(self, content, level, lineNumber):
        new_node = Node(content, level, lineNumber, None)

        # If the graph is empty, set the new node as the root
        if self.root is None:
            self.root = new_node
            self.levels[level] = [new_node]  # Create a list for the first level
        else:
            parent_level = level - 1
            if parent_level in self.levels:
                parent_nodes = self.levels[parent_level]
                parent_node = parent_nodes[-1]  # Get the last node at the parent level
                parent_node.children.append(new_node)
                new_node.parent = parent_node
                if level in self.levels:
                    self.levels[level].append(new_node)
                else:
                    self.levels[level] = [new_node]

    def display(self, node, level=0):
        if node is not None:
            print("  " * level + f"Level {node.getLevel()}: {node.getContent()} (Line {node.getLineNumber()})")
            for child in node.children:
                self.display(child, level + 1)

# Example usage:
graph = Graph()
graph.add_node("Root", 0, 1)
graph.add_node("Child 1", 1, 2)
graph.add_node("Child 2", 1, 3)
graph.add_node("Grandchild 1", 2, 4)
graph.display(graph.root)
