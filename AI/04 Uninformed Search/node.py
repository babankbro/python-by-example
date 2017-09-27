class Node:
    
    def __init__(self, name):
        self.name = name
        self.connect = {}
        
    def __str__(self):
        return "Node [Name: "+self.name+", Connect:"+str(self.connect)+"]"

    def __repr__(self):
        return str(self)
