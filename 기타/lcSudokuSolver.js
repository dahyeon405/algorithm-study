// 각 cell, row, column에 대한 set을 만들어준다.
function createSet(board) {
  const row = {};
  const column = {};
  const cell = {};

  // row 만들기
  for (let i = 0; i < 9; i++) {
    row[i] = new Set(board[i]);
  }

  // column 만들기
  for (let i = 0; i < 9; i++) {
    for (let k = 0; k < 9; k++) {
      if (!column[i]) column[i] = new Set();
      column[i].add(board[k][i]);
    }
  }

  // cell 만들기
  for (let i = 0; i < 9; i++) {
    for (let k = 0; k < 9; k++) {
      const idx = Math.floor(i / 3) * 3 + Math.floor(k / 3);
      if (!cell[idx]) cell[idx] = new Set();
      cell[idx].add(board[i][k]);
    }
  }

  return { row, column, cell };
}

var solveSudoku = function (board) {
  const { row, column, cell } = createSet(board);

  function isNoDuplicate(i, k, num) {
    let cellIdx = Math.floor(i / 3) * 3 + Math.floor(k / 3);
    if (!row[i].has(num) && !column[k].has(num) && !cell[cellIdx].has(num)) return true;
    return false;
  }

  function DFS(i, k) {
    if (i === 8 && k === 9) {
      return true;
    } else if (k === 9) {
      k = 0;
      i++;
    }

    if (board[i][k] === ".") {
      let found = false;
      for (let j = 1; j <= 9; j++) {
        let jStr = "" + j;
        if (isNoDuplicate(i, k, jStr)) {
          found = true;
          board[i][k] = jStr;

          let cellIdx = Math.floor(i / 3) * 3 + Math.floor(k / 3);
          row[i].add(jStr);
          column[k].add(jStr);
          cell[cellIdx].add(jStr);

          let result = DFS(i, k + 1);
          if (result) {
            return true;
          } else {
            row[i].delete(jStr);
            column[k].delete(jStr);
            cell[cellIdx].delete(jStr);
            found = false;
            board[i][k] = ".";
            continue;
          }
        } else continue;
      }
      if (!found) return false;
    } else {
      return DFS(i, k + 1);
    }
  }

  DFS(0, 0);
  return board;
};
