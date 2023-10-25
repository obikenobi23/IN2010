from Node import Node, NodeWeighted, NodeUnWeighted, NodeDirected, NodeUndirected
from Graf import Graf
from Dijkstra import Dijkstra

weighted = True
unweighted = False

A = NodeDirected("A", weighted)
B = NodeDirected("B", weighted)
C = NodeDirected("C", weighted)
D = NodeDirected("D", weighted)
E = NodeDirected("E", weighted)
F = NodeDirected("F", weighted)

A.addNeighbour(B, 10)
B.addNeighbour(C, 20)
A.addNeighbour(D, 15)
C.addNeighbour(D, 5)
D.addNeighbour(F, 30)
C.addNeighbour(E, 40)

A.addNeighbourBulk([C, D, E], [5, 15, 40])

G = Graf()
G.buildGrafFromNode(A)

DijkstraSearchAlgorithm = Dijkstra(G)

print(DijkstraSearchAlgorithm.search(G))
print(DijkstraSearchAlgorithm.search(G, root=A))
print(DijkstraSearchAlgorithm.search(G, endpoint=A))
print(DijkstraSearchAlgorithm.search(G, root=A, endpoint=A))