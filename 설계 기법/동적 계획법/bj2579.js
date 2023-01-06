// const fs = require("fs");
// const inputs = fs.readFileSync("/dev/stdin").trim().split("\n").map(Number);
// const N = inputs.shift();

function solution(N, stairs) {
  const dp = Array.from({ length: N + 1 }, () => 0);

  for (let i = 0; i < N; i++) {
    // 계단 한 개 -> i-2 밟고, i 밟고, i+1 밟고
    if (i <= 1) {
      dp[i + 1] = Math.max(dp[i + 1], dp[i] + stairs[i]);
    } else {
      dp[i + 1] = Math.max(dp[i + 1], dp[i - 2] + stairs[i - 1] + stairs[i]);
    }

    // 계단 두 개
    if (i + 2 <= N) {
      dp[i + 2] = Math.max(dp[i + 2], dp[i] + stairs[i + 1]);
    }
  }

  return dp[N];
}

// console.log(solution(N, inputs));
