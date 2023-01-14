/**
 * @param {string} digits
 * @return {string[]}
 */
var letterCombinations = function (digits) {
  const letterObj = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  const result = [];

  function DFS(idx, str) {
    if (idx >= digits.length) {
      if (digits.length === 0) return;
      result.push(str);
      return;
    }
    const letters = letterObj[digits[idx]];
    for (let i = 0; i < letters.length; i++) {
      DFS(idx + 1, str + letters[i]);
    }
  }

  DFS(0, "");

  return result;
};
var letterCombinations = function (digits) {
  const letterObj = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  const result = [];

  function DFS(idx, str) {
    if (idx >= digits.length) {
      if (digits.length === 0) return;
      result.push(str);
      return;
    }
    const letters = letterObj[digits[idx]];
    for (let i = 0; i < letters.length; i++) {
      DFS(idx + 1, str + letters[i]);
    }
  }

  DFS(0, "");

  return result;
};
