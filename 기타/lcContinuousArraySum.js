// 내 원래 풀이
// O(N^2)라 시간 초과가 나온다...
var checkSubarraySum = function (nums, k) {
  let numSet = new Set();
  for (let i = 0; i < nums.length; i++) {
    let remainder = nums[i] % k;
    if (remainder === 0 && numSet.has(0)) return true;
    if (numSet.has(k - remainder)) return true;
    let newSet = new Set();
    for (let n of numSet) {
      newSet.add((n + remainder) % k);
    }
    newSet.add(remainder);
    numSet = newSet;
  }
  return false;
};

// O(n)으로 풀 수 있는 풀이
// 0...i 까지 더한 sum의 나머지를 기록
// 같은 나머지가 두 번 등장했다면, 합이 k*n인 게 있다는 뜻!!
var checkSubarraySum = function (nums, k) {
  let remainderHashMap = new Map();

  let sum = 0;
  remainderHashMap.set(0, 0);
  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    let remainder = sum % k;
    if (!remainderHashMap.has(remainder)) {
      remainderHashMap.set(remainder, i + 1);
    } else {
      if (remainderHashMap.get(remainder) === i) continue;
      return true;
    }
  }
  return false;
};
