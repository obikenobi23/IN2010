from itertools import zip_longest as ignore_weights

class Node:
    
    def __init__(self, value=None, weighted=False) -> None:
        self.value = value
        self.instance = NodeWeighted() if weighted else NodeUnWeighted()
    
    # --------------------
    # Write-methods
    # --------------------
    def updateValue(self, newValue):
        self.value = newValue
    
    # --------------------
    # Read-methods
    # --------------------
    def getNeighbours(self):
        return self.instance.Neighbours
    
    def getValue(self):
        return self.value
    
    def getInstance(self):
        return self.instance
    
    def getPaths(self):
        return self.instance.getPaths()
    
    def getPathsEndsOnly(self):
        return self.instance.getPathsEndOnly()
    
    def getNeighboursValue(self):
        allNeighboursValue = set()

        for neighbours in self.instance.Neighbours:
            allNeighboursValue.add(neighbours.getValue())

        return allNeighboursValue
    
    def getNeighboursWeight(self):
        return self.instance.getNeighboursWeight()
    
    def getNeighbourWeight(self, Node):
        return self.instance.getNeighbourWeight(Node)
    
    def getNeighboursWeightAndValue(self):
        return self.instance.getNeighboursWeightAndValue()


# --------------------
# --------------------
## Composition with delegation
# --------------------
# --------------------
class NodeUnWeighted():
    def __init__(self) -> None:
        self.Neighbours = set()

    # --------------------
    # Write-methods
    # --------------------
    def addToNeighbours(self, Node, weight=None):
        self.Neighbours.add(Node)

    def removeNeighbour(self, Node):
        self.Neighbours.remove(Node)
    
    #--------------------
    # Read-methods
    #--------------------    
    def getPathsEndOnly(self):
        paths = set()

        for endpoints in self.Neighbours:
            paths.add((endpoints,))
        
        return paths

class NodeWeighted():
    def __init__(self) -> None:
        self.Neighbours = {}
    
    # --------------------
    # Write-methods
    # --------------------
    def addToNeighbours(self, Node, weight):
        self.Neighbours[Node] = weight
    
    def removeNeighbour(self, Node):
        self.Neighbours[Node] = None

    def updateWeight(self, Node, weight):
        if bool(self.Neighbours[Node]):
            self.Neighbours[Node] = weight
        else:
            print("ERROR: Edge not initialized.")
            print("Error in:", self, "and", Node)
            exit(2)

    # --------------------
    # Read-methods
    # --------------------
    def getNeighbours(self):
        allNeighbours = set()
        for neighbours in self.Neighbours.keys():
            allNeighbours.add(neighbours)
        
        return allNeighbours
    
    def getPaths(self):
        paths = set()
        for neighbour, weight in self.Neighbours.items():
            paths.add((self, neighbour, weight))
        
        return paths


    def getPathsWeight(self):
        paths = set()

        for weight in self.Neighbours.values():
            paths.add(weight)
        
        return paths
    
    def getPathsEndOnly(self):
        paths = set()

        for endpointsAndWeights in self.Neighbours.items():
            paths.add(endpointsAndWeights)
        
        return paths

    def getNeighboursValue(self):
        allNeighboursValue = set()

        for neighbours in self.Neighbours.keys():
            allNeighboursValue.add(neighbours.getValue())

        return allNeighboursValue
    
    def getNeighboursWeight(self):
        allNeighboursWeight = set()

        for weights in self.Neighbours.values():
            allNeighboursWeight.add(weights)

        return allNeighboursWeight
    
    def getNeighbourWeight(self, Node):
        return self.Neighbours[Node]
    
    def getNeighboursWeightAndValue(self):
        allNeighboursWeightAndValue = set()

        for neighbour in self.Neighbours.items():
            allNeighboursWeightAndValue.add((neighbour, neighbour.getValue()))

        return allNeighboursWeightAndValue

# --------------------
# --------------------
## Inherited classses
# --------------------
# --------------------
class NodeDirected(Node):
    def __init__(self, value=None, directed=False) -> None:
        super().__init__(value, directed)
    
    # --------------------
    # Write-methods
    # --------------------
    def addNeighbour(self, Node, weight=None):
        self.instance.addToNeighbours(Node, weight)
        Node.instance.addToNeighbours(self, weight)
    
    def addNeighbourBulk(self, nodes, listOfWeights=[]):
        for neighbours, weights in ignore_weights(nodes, listOfWeights):
            self.instance.addToNeighbours(neighbours, weights)
    
    # --------------------
    # Read-methods
    # --------------------



class NodeUndirected(Node):
    def __init__(self, value=None, directed=False) -> None:
        super().__init__(value, directed)
    # --------------------
    # Write-methods
    # --------------------
    def addNeighbour(self, Node, weight=None):
        self.instance.addToNeighbours(Node, weight)
        Node.instance.addToNeighbours(self, weight)
    
    def addNeighbourBulk(self, *nodes, weights=[]):
        for neighbours, weights in ignore_weights(nodes, weights):
            self.instance.addToNeighbours(neighbours, weights)
            neighbours.instance.addToNeighbours(self, weights)

    
    def removeNeighbour(self, Node):
        self.instance.removeNeighbour(Node)
        for neighbours in self.instance.getNeighbours():
            neighbours.instance.removeNeighbour(self)
    
    # --------------------
    # Read-methods
    # --------------------