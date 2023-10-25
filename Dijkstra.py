import sys
import random
from collections import defaultdict
from Node import Node, NodeWeighted
from Graf import Graf

class Dijkstra:
    def __init__(self, graf) -> None:
        self.Graf = graf
        self.Paths = defaultdict(lambda : sys.maxsize)
        self.searchThru()
    
    #--------------------
    # Write-methods
    #--------------------
    def search(self, newGraf=None, root=None, endpoint=None):
        V = self.Graf.getVertices()

        # --------------------
        # Typechecking
        # --------------------
        for node in V:
            if not isinstance(node.getInstance(), NodeWeighted):
                print("ERROR: Graf er ikke vektet")
                exit(2)
        
        # --------------------
        # "Caching"
        # --------------------
        isNewGraf = bool(newGraf)
        if isNewGraf and self.Graf != newGraf:
            self.Shortest = (Node, 0)
            self.Paths = defaultdict(lambda : sys.maxsize)
            self.Graf = newGraf
            self.searchThru()
        
        if root:
            if endpoint:
                return self.Paths[(root, endpoint)]
            else:
                return [path[1] for path in self.Paths.items() if path[0]==root]
        else:
            if endpoint:
                return [path[1] for path in self.Paths.items() if path[1]==endpoint]
            else:
                return self.Paths

    
    def searchThru(self):
        def searchRec(current, goal, unvisited, pathTracked, distance):

            openPaths = [endpoints for endpoints in current.getPathsEndsOnly() if endpoints in unvisited]
            # End of search
            if openPaths == []:
                return pathTracked, sys.maxsize
            
            potentialTracks = set()

            for validSearches in openPaths:
            
                distanceFromCurrent = current.getNeighbourWeight(validSearches)
                if validSearches == goal:
                    potentialTracks.add((pathTracked + [validSearches], distanceFromCurrent + distance))
                else:
                    potentialTracks.add(searchRec(validSearches, goal, unvisited.remove(validSearches), pathTracked + [validSearches], distance + distanceFromCurrent))
            
            potentialTracks.sort(lambda x : x[1])
            return potentialTracks[0]
        
        V, E = self.Graf.getVertices(), self.Graf.getEdges()

        for root in V:
            root_neighbours = list(root.getNeighbours())
            unvisited = list(V.copy())

            unvisited.remove(self.addDijkstra((root, root), 0))

            for index, goals in enumerate(unvisited):
                path, distance = searchRec(root, goals, unvisited[index:], [root], 0)
                self.addDijkstra(tuple(path), distance)

            # Hent listen med vektede kanter: lag en sti av dem, returner stien og sum av vekt



                
    def addDijkstra(self, path, distance):
        self.Paths[path] = distance
        return path[-1]


    #--------------------
    # Read-methods
    #--------------------
    def printLengths(self):
        print(self.Edges)