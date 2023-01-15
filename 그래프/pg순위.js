// 플로이드-워셜 알고리즘
function solution(n, results) {
  var answer = 0;

  // 표 만들기
  const board = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(0));

  // 초기 값 설정
  results.forEach((el) => {
    let [A, B] = el;
    board[A][B] = 1;
  });

  // 플로이드-워셜 알고리즘
  for (let i = 1; i <= n; i++) {
    for (let j = 1; j <= n; j++) {
      if (board[i][j] !== 0) {
        for (let k = 1; k <= n; k++) {
          if (board[k][i] === 1) board[k][j] = 1;
        }
      }
    }
  }

  let answer = 0;
  for (let i = 1; i <= n; i++) {
    let sum = 0;
    // row sum
    sum += board[i].reduce((a, b) => a + b, 0);

    for (let k = 1; k <= n; k++) {
      sum += board[k][i];
    }

    if (sum === n - 1) answer++;
  }

  return answer;
}
