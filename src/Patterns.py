# A  graph structure that store patterns extract
# directly from json objects, store pattern in a tree
# and count the times each pattern appears in the file.

class Patterns:
    
    def __init__(self, name):
        ## Name of the pattern.
        self.name = name
        ## Count of the current pattern appears in the file
        self.count = 0
        ## All nodes after this pattern
        self.next = list()
    
    def isInList(self, pattern):
        ## Search if a pattern already exist in the next list.
        for i in range(len(self.next)):
            if (pattern.name == self.next[i].name):
                return i 
            
        return -1
                
    def addNode(self, pattern):
        self.next.append(pattern)
        return self.next.index(pattern)
        
# root = Patterns("root")    
# myClass = Patterns("new Name")
# mayClass2 = Patterns("new Name")
# index = root.addNode(myClass)
# number = root.isInList(mayClass2)
# print root.next[number].name,index
