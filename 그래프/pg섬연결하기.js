// 크러스컬 알고리즘

class UnionFind {
  constructor(n) {
    this.par = Array.from({ length: n }, () => -1);
    this.siz = Array.from({ length: n }, () => 1);
  }

  root(x) {
    if (this.par[x] === -1) return x;
    return (this.par[x] = this.root(this.par[x]));
  }

  unite(x, y) {
    let root_x = this.root(x);
    let root_y = this.root(y);

    if (root_x === root_y) return false;

    if (this.siz[root_x] < this.siz[root_y]) {
      [root_x, root_y] = [root_y, root_x]; //swap
    }

    this.par[root_y] = root_x;
    this.siz[root_x] += this.siz[root_y];

    return true;
  }

  issame(x, y) {
    if (this.root(x) === this.root(y)) return true;
    return false;
  }
}

function solution(n, costs) {
  let sortedCosts = costs.sort((a, b) => a[2] - b[2]); // cost 적은 순서대로 정렬

  const uf = new UnionFind(n);
  let cost = 0;
  for (let i = 0; i < sortedCosts.length; i++) {
    if (uf.issame(sortedCosts[i][0], sortedCosts[i][1])) continue;
    uf.unite(sortedCosts[i][0], sortedCosts[i][1]);
    cost += sortedCosts[i][2];
  }

  return cost;
}
