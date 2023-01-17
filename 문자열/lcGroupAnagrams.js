var groupAnagrams = function (strs) {
  let sortedStrs = strs.map((str) => str.split("").sort().join(""));
  let anagramMap = new Map();

  for (let i = 0; i < sortedStrs.length; i++) {
    if (!anagramMap.has(sortedStrs[i])) anagramMap.set(sortedStrs[i], [strs[i]]);
    else anagramMap.get(sortedStrs[i]).push(strs[i]);
  }

  let result = [];
  for (let values of anagramMap.values()) {
    result.push(values);
  }

  return result;
};
