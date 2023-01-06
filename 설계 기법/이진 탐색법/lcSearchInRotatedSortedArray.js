var search = function (nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while (left < right) {
    let mid = left + Math.floor((right - left) / 2);
    if (nums[mid] === target) return mid;
    if (nums[left] > nums[right]) {
      // 뒤집힌 상태
      if (target > nums[mid]) {
        if (target <= nums[right]) left = mid + 1;
        else right = mid + 1;
      } else {
        if (target <= nums[right]) {
          left = mid + 1;
        } else right = mid - 1;
      }
    } else {
      if (target > nums[mid]) left = mid + 1;
      else right = mid - 1;
    }
    console.log(mid, left, right);
  }
  if (nums[right] !== target) return -1;
  return right;
};

search([5, 1, 3], 5);
