import random

class Separasjonsnoder:
    def __init__(self) -> None:
        self.depth = {}
        self.low = {}
        self.seps = set()
    
    def getValues(self):
        sepsValues = set()
        for sep in self.seps:
            sepsValues.add(sep.getValue())
        return sepsValues


    def separationVertices(self, G):
        self.seps = set()
        self.V = G.getVertices()
        self.E = G.getEdges()
        s = random.choice(tuple(self.V))
        print("rotnode", s.getValue())
        self.depth[s] = 0
        self.low[s] = 0
        children = 0

        for (s, u) in [p for p in s.getPaths()]:
            if u not in self.depth.keys():
                self.SepRec(G, s, u, 1)
                children += 1
        
        if children > 1:
            self.seps.add(s)
        return self.seps
    
    def SepRec(self, G, p, u, d): # Graf, parent, search-from-node, depth
        self.E = G.getEdges()
        self.depth[u] = d
        self.low[u] = d

        for (u, v) in [p for p in u.getPaths()]:
            if v == p:
                continue
            if v in self.depth:
                self.low[u] = min(self.low[u], self.depth[v])
                continue
            
            self.SepRec(G, u, v, d+1)
            self.low[u] = min(self.low[u], self.low[v])
            if d <= self.low[v]:
                self.seps.add(u)