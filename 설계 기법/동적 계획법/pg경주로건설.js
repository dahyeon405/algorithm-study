/*
function solution(board) {
  var answer = 0;
  const N = board.length;

  const dirs = [
    [1, 0, 1],
    [-1, 0, 1],
    [0, 1, 0],
    [0, -1, 0],
  ];
  const check = Array.from({ length: N }, () => new Array(N).fill(false));
  const dp = Array.from({ length: N }, () => new Array(N));
  dp.forEach((el, index) => {
    dp[index] = Array.from({ length: N }, () => new Array(N).fill(Number.MAX_SAFE_INTEGER));
  });

  dp[0][0][0] = 0;
  dp[0][0][1] = 0;

  let minFare = Number.MAX_SAFE_INTEGER;

  function dfs(i, k, fare, dir) {
    if (fare > minFare) return;

    // dp 업데이트
    if (dir !== undefined) {
      if (dp[i][k][dir] <= fare) return;
      else dp[i][k][dir] = fare;
    }

    // 끝까지 도달할 시 업데이트 해주고 중단
    if (i === N - 1 && k === N - 1) {
      if (minFare > fare) minFare = fare;
      return;
    }

    dirs.forEach((el) => {
      let m = el[0] + i;
      let n = el[1] + k;
      let nextDir = el[2];

      if (m >= N || m < 0 || n >= N || n < 0) return;

      if (!check[m][n] && board[m][n] === 0) {
        let f = dir === undefined || nextDir === dir ? 100 : 600;
        check[m][n] = true;
        dfs(m, n, fare + f, nextDir);
        check[m][n] = false;
      }
    });
  }

  dfs(0, 0, 0, undefined);

  return minFare;
}
*/

function solution(board) {
  var answer = 0;
  const N = board.length;

  const dirs = [
    [1, 0, 1],
    [-1, 0, 1],
    [0, 1, 0],
    [0, -1, 0],
  ];
  const check = Array.from({ length: N }, () => new Array(N).fill(false));
  const dp = Array.from({ length: N }, () => new Array(N).fill(new Array(2).fill(Number.MAX_SAFE_INTEGER)));

  dp[0][0][0] = 0;
  dp[0][0][1] = 0;

  let minFare = Number.MAX_SAFE_INTEGER;

  function dfs(i, k, fare, dir) {
    if (fare > minFare) return;

    // dp 업데이트
    if (dir !== undefined) {
      if (dp[i][k][dir] <= fare) return;
      else dp[i][k][dir] = fare;
    }

    // 끝까지 도달할 시 업데이트 해주고 중단
    if (i === N - 1 && k === N - 1) {
      if (minFare > fare) minFare = fare;
      return;
    }

    dirs.forEach((el) => {
      let m = el[0] + i;
      let n = el[1] + k;
      let nextDir = el[2];

      if (m >= N || m < 0 || n >= N || n < 0) return;

      if (!check[m][n] && board[m][n] === 0) {
        let f = dir === undefined || nextDir === dir ? 100 : 600;
        check[m][n] = true;
        dfs(m, n, fare + f, nextDir);
        check[m][n] = false;
      }
    });
  }

  dfs(0, 0, 0, undefined);

  return minFare;
}
