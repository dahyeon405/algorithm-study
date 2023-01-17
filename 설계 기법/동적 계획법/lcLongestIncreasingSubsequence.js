var lengthOfLIS = function (nums) {
  let dp = new Array(nums.length).fill(0);

  for (let i = 0; i < nums.length; i++) {
    let max = 0;
    for (let k = 0; k < i; k++) {
      if (nums[k] < nums[i] && dp[k] > max) {
        max = dp[k];
      }
    }
    dp[i] = max + 1;
  }

  return Math.max(...dp);
};
