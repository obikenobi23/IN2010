from Node import *
from Dijkstra import *

class Map:
    def __init__(self) -> None:
        self.Nodes = {}
    
    def addNode(self, Node, weights):
        for neighbours, distance in Node.getNeighbours(), weights:
            self.Nodes[(Node, neighbours)] = distance