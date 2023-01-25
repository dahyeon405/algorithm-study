// 처음 풀이. 효율성 통과 못함.
function solution(board) {
  function isSquare(i, k, length) {
    for (let j = i; j < i + length; j++) {
      for (let m = k; m < k + length; m++) {
        if (board[j][m] !== 1) return false;
      }
    }
    return true;
  }

  let max = 0;
  const m = board.length;
  const n = board[0].length;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (board[i][j] !== 1) continue;
      let maxLength = Math.min(m - i, n - j);
      if (maxLength <= max) continue;

      if (max === 0) max = 1;
      let length = max + 1;

      while (length <= maxLength) {
        if (isSquare(i, j, length) && length > max) {
          max = length;
          length++;
        } else break;
      }
    }
  }

  return max * max;
}

// dp 사용한 풀이법
function solution(board) {
  for (let i = 1; i < board.length; i++) {
    for (let k = 1; k < board[0].length; k++) {
      if (board[i][k] === 0) continue;
      let n = board[i - 1][k - 1];
      let n_1 = board[i][k - 1];
      let n_2 = board[i - 1][k];
      board[i][k] = Math.min(n_1, n_2, n) + 1;
    }
  }

  let max = 0;
  for (let i = 0; i < board.length; i++) {
    for (let k = 0; k < board[0].length; k++) {
      if (board[i][k] > max) {
        max = board[i][k];
      }
    }
  }

  return max * max;
}
