# dfs로 풀 시 런타임 에러 남
# 튜플도 dict의 key로 활용 가능

class UnionFind:
    def __init__(self, x, y, maps):
        self.par = {}
        self.siz = {}
        for i in range(x):
            for k in range(y):
                self.par[(i, k)] = -1
                self.siz[(i, k)] = int(maps[i][k]) if maps[i][k] != "X" else 0
                
    def root(self, tp):
        x, y = tp
        if self.par[(x, y)] == -1: return (x, y)
        self.par[(x, y)] = self.root(self.par[(x, y)])
        return self.par[(x, y)]
    
    def unite(self, tp_1, tp_2):
        tp_1 = self.root(tp_1)
        tp_2 = self.root(tp_2)
        if tp_1 == tp_2: return
        self.par[tp_2] = tp_1
        self.siz[tp_1] += self.siz[tp_2]
        
    def getSizes(self):
        sizes = []
        for key, val in self.siz.items():
            if (self.par[key] == -1 and val != 0):
                sizes.append(val)
        return sizes
    
    
def solution(maps):
    
    uf = UnionFind(len(maps), len(maps[0]), maps)
    for i in range(len(maps)):
        for k in range(len(maps[0])):
            if maps[i][k] == "X": continue
            if (i+1 < len(maps) and maps[i+1][k] != "X"): uf.unite((i, k), (i+1, k))
            if (k+1 < len(maps[0]) and maps[i][k+1] != "X"): uf.unite((i, k), (i, k+1))
    
    sizes = uf.getSizes()
    if len(sizes) == 0: return [-1]
    sizes.sort()
    
    return sizes