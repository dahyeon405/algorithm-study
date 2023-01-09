// UnionFind 풀이법. Runtime, Memory 모두 좋지 않음
class Unionfind {
  constructor(N) {
    this.par = Array.from({ length: N }, () => -1);
    this.siz = Array.from({ length: N }, () => 1);
  }

  root(x) {
    if (this.par[x] === -1) return x;
    return (this.par[x] = this.root(this.par[x]));
  }

  unite(x, y) {
    let rootX = this.root(x);
    let rootY = this.root(y);
    if (rootX === rootY) return false;
    if (this.siz[rootX] < this.siz[rootY]) {
      let tmp = rootX;
      rootX = rootY;
      rootY = tmp;
    }
    this.par[rootY] = rootX;
    this.siz[rootX] += this.siz[rootY];
    return true;
  }

  size(x) {
    return this.siz[this.root(x)];
  }
}

var solve = function (board) {
  let coord_O = [];
  const rowCnt = board.length;
  const columnCnt = board[0].length;
  for (let i = 0; i < rowCnt; i++) {
    for (let k = 0; k < columnCnt; k++) {
      if (board[i][k] === "O") coord_O.push([i, k]);
    }
  }
  const unionfind = new Unionfind(coord_O.length);
  for (let i = 0; i < coord_O.length; i++) {
    for (let k = i + 1; k < coord_O.length; k++) {
      if (isAdjacent(coord_O[i], coord_O[k])) {
        unionfind.unite(i, k);
      }
    }
  }
  const invalidRoot = new Set();
  for (let i = 0; i < coord_O.length; i++) {
    if (isBorder(coord_O[i], columnCnt, rowCnt)) {
      invalidRoot.add(unionfind.root(i));
    }
  }
  for (let i = 0; i < coord_O.length; i++) {
    if (!invalidRoot.has(unionfind.root(i))) {
      board[coord_O[i][0]][coord_O[i][1]] = "X";
    }
  }
  return board;
};

function isBorder(coord, columnCnt, rowCnt) {
  const [i, k] = coord;
  if (i === 0 || k === 0 || i === rowCnt - 1 || k === columnCnt - 1) return true;
  return false;
}

function isAdjacent(coord_1, coord_2) {
  if (coord_1[0] === coord_2[0] && Math.abs(coord_1[1] - coord_2[1]) === 1) return true;
  if (coord_1[1] === coord_2[1] && Math.abs(coord_1[0] - coord_2[0]) === 1) return true;
  return false;
}

// dfs 풀이법 (최종 솔루션! 메모리 절약)
// 불가능한 좌표(O가 가장자리에 있는 것)에서부터 시작, dfs로 탐색하면서 #으로 표시
// #으로 표시된 것들은 X로 치환 불가능한 O이므로 마지막에 O로 바꿔줌
// 그 외 O, X는 모두 X로 바꿔줌

var solve = function (board) {
  const rowCnt = board.length;
  const columnCnt = board[0].length;

  for (let i = 0; i < rowCnt; i++) {
    for (let k = 0; k < columnCnt; k++) {
      if (board[i][k] === "O" && (i === 0 || k === 0 || i === rowCnt - 1 || k === columnCnt - 1)) {
        dfs(i, k, board);
      }
    }
  }
  for (let i = 0; i < rowCnt; i++) {
    for (let k = 0; k < columnCnt; k++) {
      if (board[i][k] === "#") board[i][k] = "O";
      else board[i][k] = "X";
    }
  }
};

function dfs(i, k, board) {
  if (i < 0 || i >= board.length || k < 0 || k >= board[0].length) return;
  if (board[i][k] === "#" || board[i][k] === "X") return;
  board[i][k] = "#";
  dfs(i + 1, k, board);
  dfs(i, k + 1, board);
  dfs(i - 1, k, board);
  dfs(i, k - 1, board);
}
