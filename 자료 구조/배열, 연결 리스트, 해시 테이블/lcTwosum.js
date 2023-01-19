var twoSum = function (nums, target) {
  const sortedNums = [...nums].sort((a, b) => a - b);

  let i = 0;
  let k = nums.length - 1;

  while (true) {
    let sum = sortedNums[i] + sortedNums[k];
    if (sum === target) {
      return [nums.indexOf(sortedNums[i]), nums.lastIndexOf(sortedNums[k])];
    } else if (sum < target) {
      i++;
    } else k--;
  }
};
