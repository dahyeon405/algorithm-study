var longestPalindrome = function (s) {
  let maxLength = 0;
  let maxStr = "";

  for (let i = 0; i < s.length; i++) {
    let j = i;
    while (s[i] === s[j]) {
      j++;
    }
    j--;
    let k = 0;
    while (i - k >= 0 && j + k < s.length && s[i - k] === s[j + k]) {
      if (j + k - i + k + 1 > maxLength) {
        maxStr = s.slice(i - k, j + k + 1);
        maxLength = j + k - i + k + 1;
      }
      k++;
    }
    i = j;
  }
  return maxStr;
};
