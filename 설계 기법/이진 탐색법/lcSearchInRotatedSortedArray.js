var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right - 1) {
    let mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    if (nums[left] > nums[right]) {
      // 뒤집힌 상태
      if (nums[mid] > nums[right]) {
        if (target >= nums[left] && target < nums[mid]) right = mid;
        else left = mid;
      } else {
        if (target <= nums[right] && target > nums[mid]) left = mid;
        else right = mid;
      }
    } else {
      if (target > nums[mid]) left = mid;
      else right = mid;
    }
  }
  if (nums[left] == target) return left;
  if (nums[right] == target) return right;
  return -1;
};
