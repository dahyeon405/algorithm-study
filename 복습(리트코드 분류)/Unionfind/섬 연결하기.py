class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.siz = [1]*n
        
    def root(self, x):
        if self.par[x] == -1: return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y: return
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.par[y] = x
        self.siz[x] += self.siz[y]
        
    def size(x):
        return self.siz[self.root(x)]
        
def solution(n, costs):
    
    sortedCosts = sorted(costs, key = lambda x: x[2])
    
    uf = Unionfind(n)
    
    total = 0
    for a, b, d in sortedCosts:
        if uf.root(a) == uf.root(b): continue
        uf.unite(a, b)
        total += d
    
    return total