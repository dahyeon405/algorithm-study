var twoSum = function (nums, target) {
  const sortedNums = [...nums].sort((a, b) => a - b);

  let i = 0;
  let k = nums.length - 1;

  while (true) {
    let sum = sortedNums[i] + sortedNums[k];
    if (sum === target) {
      if (sortedNums[i] === sortedNums[k]) {
        let firstIndex = nums.indexOf(sortedNums[i]);
        let nextIndex = nums.slice(firstIndex + 1).indexOf(sortedNums[i]);
        return [firstIndex, nextIndex];
      }
      return [nums.indexOf(sortedNums[i]), nums.indexOf(sortedNums[k])];
    } else if (sum < target) {
      i++;
    } else k--;
  }
};
