var findSubstring = function (s, words) {
  let wordCountMap = new Map();
  words.forEach((word) => {
    if (wordCountMap.has(word)) wordCountMap.set(word, wordCountMap.get(word) + 1);
    else wordCountMap.set(word, 1);
  });

  let subStrLength = words[0].length * words.length;
  let result = [];
  for (let i = 0; i <= s.length - subStrLength; i++) {
    if (isPermutation(s.slice(i, i + subStrLength), words, wordCountMap)) result.push(i);
  }
  return result;
};

function isPermutation(subStr, words, wordCountMap) {
  let wordLength = words[0].length;
  let wordTable = new Map();
  words.forEach((word) => {
    wordTable.set(word, 0);
  });
  for (let i = 0; i < subStr.length; i += wordLength) {
    let w = subStr.slice(i, i + wordLength);
    wordTable.set(w, wordTable.get(w) + 1);
  }
  for (let [key, value] of wordTable.entries()) {
    if (wordCountMap.get(key) !== value) return false;
  }
  return true;
}
