// const fs = require("fs");
// const inputs = fs.readFileSync("/dev/stdin").toString().split("\n");
// const [N, M] = inputs[0].split(" ").map(Number);
// const m = inputs[1].split(" ").map(Number);
// const c = inputs[2].split(" ").map(Number);

function solution(N, M, m, c) {
  let sum = m.reduce((a, b) => a + b, 0);
  let maxByte = sum - M;

  let dp = Array.from({ length: N + 1 }, () => Array(maxByte + 1).fill(0));

  for (let i = 0; i < N; i++) {
    for (let k = 0; k <= maxByte; k++) {
      // m[i] 포함
      if (k - m[i] >= 0) {
        dp[i + 1][k] = Math.max(dp[i][k], dp[i][k - m[i]] + c[i]);
      }

      // m[i] 미포함
      dp[i + 1][k] = Math.max(dp[i + 1][k], dp[i][k]);
    }
  }

  let byteSum = c.reduce((a, b) => a + b, 0);
  let answer = byteSum - dp[N][maxByte];

  return answer;
}

console.log(solution(5, 60, [30, 10, 20, 35, 40], [3, 0, 3, 5, 4]));

// 시간 초과 (미해결)
