var isValidSudoku = function (board) {
  const rowsArr = Array.from({ length: 9 }, () => new Set());
  const columnsArr = Array.from({ length: 9 }, () => new Set());
  const boxesArr = Array.from({ length: 9 }, () => new Set());

  for (let i = 0; i < 9; i++) {
    for (let k = 0; k < 9; k++) {
      const num = board[i][k];
      if (num === ".") continue;
      const boxIndex = 3 * Math.floor(i / 3) + Math.floor(k / 3);
      if (rowsArr[i].has(num) || columnsArr[k].has(num) || boxesArr[boxIndex].has(num)) return false;
      rowsArr[i].add(num);
      columnsArr[k].add(num);
      boxesArr[boxIndex].add(num);
    }
  }

  return true;
};
