#from Dijkstra import Dijkstra
#from Map import Map
from Node import Node, NodeWeighted, NodeUnWeighted, NodeDirected, NodeUndirected
from Separasjonsnoder import Separasjonsnoder
from Graf import Graf

weighted = True
unweighted = False

A = NodeUndirected("A", unweighted)
B = NodeUndirected("B", unweighted)
C = NodeUndirected("C", unweighted)
D = NodeUndirected("D", unweighted)
E = NodeUndirected("E", unweighted)
F = NodeUndirected("F", unweighted)

A.addNeighbourBulk([B, D])
B.addNeighbour(C)
C.addNeighbourBulk([D, E])
D.addNeighbour(F)

print("A", A.getNeighboursValue())
print("B", B.getNeighboursValue())
print("C", C.getNeighboursValue())
print("D", D.getNeighboursValue())
print("E", E.getNeighboursValue())
print("F", F.getNeighboursValue())

G = Graf()
G.buildGrafFromNode(A)

print(G.getVerticesValues(), G.getEdgesValues())
#print(G.getEdges())

findSep = Separasjonsnoder()
separasjonsnoder = findSep.separationVertices(G)
print("separasjonsnoder", findSep.getValues())