class Graph:
    
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, node):
        self.nodes[node.name] = node;
    
    def connect(self, name1, name2):
        node1 = self.nodes[name1]
        node2 = self.nodes[name2]
        node1.connect[name2] = node2
        node2.connect[name1] = node1
    
    def __str__(self):
        toString = ""
        for key in self.nodes:
            toString += str(self.nodes[key]) + "\n"
        return toString

class DistanceGraph:
    
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, node):
        self.nodes[node.name] = node;
    
    def connect(self, name1, name2, value):
        node1 = self.nodes[name1]
        node2 = self.nodes[name2]
        node1.connect[name2] = node2, value
        node2.connect[name1] = node1, value
    
    def __str__(self):
        toString = ""
        for key in self.nodes:
            toString += str(self.nodes[key]) + "\n"
        return toString
