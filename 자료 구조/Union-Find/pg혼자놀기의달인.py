class UnionFind:
    def __init__(self, n):
        self.par = [-1]*(n+1)        
        self.siz = [1]*(n+1)
        
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
        return

def solution(cards):
    group_counts = []
    uf = UnionFind(len(cards))
    
    for i in range(1, len(cards)+1):
        uf.unite(i, cards[i-1])
    
    for i in range(1, len(cards)+1):
        if uf.root(i) != i: continue
        group_counts.append(uf.siz[i])
        
        
    group_counts.sort(reverse=True)
    if len(group_counts) == 1: return 0