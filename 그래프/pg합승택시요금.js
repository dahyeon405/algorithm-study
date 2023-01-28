function solution(n, s, a, b, fares) {
  var answer = 0;

  const dp = Array.from({ length: n + 1 }, () => new Array(n + 1).fill(Infinity));

  // 초기화
  for (let i = 1; i <= n; i++) {
    dp[i][i] = 0;
  }
  fares.forEach((el) => {
    let [c, d, f] = el;
    dp[c][d] = f;
    dp[d][c] = f;
  });

  // 플로이드-워셜 알고리즘
  for (let i = 1; i <= n; i++) {
    for (let k = 1; k <= n; k++) {
      for (let j = 1; j <= n; j++) {
        let sum = dp[k][i] + dp[i][j];
        if (sum < dp[j][k]) {
          dp[j][k] = sum;
          dp[k][j] = sum;
        }
      }
    }
  }

  let min = Infinity;
  for (let i = 1; i <= n; i++) {
    let sum = dp[s][i] + dp[i][a] + dp[i][b];
    if (sum < min) min = sum;
  }

  return min;
}
