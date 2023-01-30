// 시간 초과 풀이
function solution(stones, k) {
  var answer = 0;

  let min = Number.MAX_SAFE_INTEGER;
  for (let i = 0; i <= stones.length - k; i++) {
    let max = Math.max(...stones.slice(i, i + k));
    if (max < min) min = max;
  }

  return min;
}

// 재귀. 효율성 시 런타임에러
// Math.max(...arr) 때문에 그런 것 같다.
function solution(stones, k) {
  let min = Number.MAX_SAFE_INTEGER;

  function findMin(arr, k) {
    if (arr.length < k) return;

    const max = Math.max(...arr);
    if (max < min) min = max;
    if (arr.length === k) return;

    let lastIndex = 0;
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] === max) {
        findMin(arr.slice(lastIndex, i), k);
        lastIndex = i + 1;
        continue;
      }
      // 마지막
      if (i === arr.length - 1) {
        findMin(arr.slice(lastIndex, i + 1), k);
      }
    }
  }

  findMin(stones, k);

  return min;
}

// 이분 탐색. 부등호가 좀 헷갈렸음.
function solution(stones, k) {
  function canPass(n) {
    let cnt = 0;
    for (let i = 0; i < stones.length; i++) {
      if (stones[i] < n) cnt++;
      else cnt = 0;
      if (cnt >= k) return false;
    }
    return true;
  }

  let left = 0;
  let right = 200000000;

  while (left < right - 1) {
    let mid = Math.floor((right + left) / 2);
    if (canPass(mid)) left = mid;
    else right = mid;
  }

  if (canPass(right)) return right;
  return left;
}
