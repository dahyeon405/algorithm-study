/**
 * @param {number[]} height
 * @return {number}
 */

// Two pointer approach
var maxArea = function (height) {
  let left = 0;
  let right = height.length - 1;

  let max = 0;
  while (left < right) {
    max = Math.max(max, (right - left) * Math.min(height[right], height[left]));
    if (height[left] < height[right]) {
      left++;
    } else right--;
  }

  return max;
};
