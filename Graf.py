class Graf:
    def __init__(self) -> None:
        self.Vertices = set()
        self.Edges = set()
    
    # --------------------
    # Write-methods
    # --------------------
    def addToGraf(self, V = set(), E = set()):
        if V:
            self.Vertices.update(V)
        if E:
            self.Edges.update(E)
    
    def buildGrafFromNode(self, Node):
        self.addToGraf({Node}, Node.getPaths())

        for neighbours in [n for n in Node.getNeighbours() if n not in self.Vertices]:
            self.buildGrafFromNode(neighbours)

    
    # --------------------
    # Read-methods
    # --------------------
    def getVertices(self):
        return self.Vertices
    def getVerticesValues(self):
        verticeList = set()
        for vertice in self.Vertices:
            verticeList.add(vertice.getValue())
        return verticeList
    
    def getEdges(self):
        return self.Edges
    def getEdgesValues(self):
        edgeList = set()
        for edge in self.Edges:
            edgeList.add(edge[0].getValue())
        return edgeList
    
    # --------------------
    # Magic methods
    # --------------------
    def __eq__(self, g):
        if not isinstance(g, Graf):
            return False
        # --------------------
        # Compare this to that
        # --------------------
        for v, e in zip(self.Vertices, self.Edges):
            if v not in g.Vertices or e not in g.Edges:
                return False
        
        # --------------------
        # Compare that to this
        # --------------------
        for v_2, e_2 in zip(g.Vertices, g.Edges):
            if v_2 not in self.Vertices or e_2 not in g.Edges:
                return False
        
        return True
        

    