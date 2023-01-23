// 첫 번째로 시도했던 풀이(실패, 오류도 하나 있음)
function solution(sticker) {
  var answer = 0;
  let max = 0;

  function pick(start, end, sum, notPickCnt) {
    if (start >= end) {
      if (sum > max) max = sum;
      return;
    }
    if (start + 1 === end) {
      sum += sticker[start];
      if (sum > max) max = sum;
      return;
    }

    if (notPickCnt === 2) {
      pick(start + 1, end, sum, 0);
    } else {
      if (start === 0) pick(start + 2, end - 1, sum + sticker[0], 0);
      else pick(start + 2, end, sum + sticker[start], 0);
      pick(start + 1, end, sum, notPickCnt + 1);
    }

    return;
  }

  pick(0, sticker.length, 0, 0);

  return max;
}

// 두 번째. dp 활용.  성공
function solution(sticker) {
  if (sticker.length === 1) return sticker[0];
  else if (sticker.length === 2) return Math.max(...sticker);

  const dp = Array.from({ length: sticker.length }, () => 0);
  const dp2 = Array.from({ length: sticker.length }, () => 0);

  dp[0] = sticker[0];
  for (let i = 1; i < sticker.length - 1; i++) {
    if (i === 1) dp[1] = Math.max(dp[0], sticker[1]);
    else dp[i] = Math.max(dp[i - 1], dp[i - 2] + sticker[i]);
  }

  dp2[1] = sticker[1];
  for (let i = 2; i < sticker.length; i++) {
    if (i === 2) dp2[2] = Math.max(dp2[1], sticker[2]);
    else dp2[i] = Math.max(dp2[i - 1], dp2[i - 2] + sticker[i]);
  }

  dp[sticker.length - 1] = Math.max(dp[sticker.length - 2], dp2[sticker.length - 1]);

  return Math.max(dp2[sticker.length - 1], dp[sticker.length - 2], dp[sticker.length - 3]);
}
