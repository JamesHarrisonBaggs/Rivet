class Patterns:
    """ A node class for the tree structure
        
        The basic tree structure for all pattern nodes,
        each node contains name of a pattern, number of count 
        of a pattern that appears in a location of the tree, and
        a list of all children nodes which are patterns that appear 
        after this pattern.
    """
    
    
    def __init__(self, name):
        """Initial the node object
            
            Function to construct the node object.
            
            Args:
                name: name of the pattern
        """
        ## Name of the pattern.
        self.name = name
        ## Count of the current pattern appears in the file
        self.count = 0
        ## All nodes after this pattern
        self.next = list()
    
    def isInList(self, pattern):
        """Check if a pattern is in the children
        
            A function checks if a given pattern is already
            exist in the children list, if already exist return 
            the index of that patter in the list, if not exist
            return -1.
            
            Args:
                pattern: pattern that need to check
            Return:
                index number of exist pattern, or -1 if pattern not exist
        """
        ## Search if a pattern already exist in the next list.
        for i in range(len(self.next)):
            if (pattern.name == self.next[i].name):
                return i 
            
        return -1
                
    def addNode(self, pattern):
        """Add a new patter to childern list
        
            A function that add a new pattern object into
            the children list and the return the index of 
            this pattern in the list.
            
            Args:
                pattern: pattern that need to be added.
            Return:
                index of the pattern that has been added.
        
        """
        self.next.append(pattern)
        return self.next.index(pattern)
