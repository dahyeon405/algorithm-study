/**
 * @param {number[]} nums
 * @return {number}
 */

// MergeSort 방식으로 구현.
// 시간, 메모리 측면에서 좋은 풀이는 아니다.
function countReversePairs(left, right, nums) {
  if (left >= right) return [0, [nums[right]]];
  let mid = left + Math.floor((right - left) / 2);
  let [leftCnt, leftArr] = countReversePairs(left, mid, nums);
  let [rightCnt, rightArr] = countReversePairs(mid + 1, right, nums);

  let mergeCnt = leftCnt + rightCnt;
  let mergedArr = [];

  let rightTwiceArr = rightArr.map((i) => 2 * i);
  let i = 0;
  let k = 0;

  while (i < leftArr.length && k < rightTwiceArr.length) {
    if (leftArr[i] > rightTwiceArr[k]) {
      mergeCnt += leftArr.length - i;
      k++;
    } else {
      i++;
    }
  }

  i = 0;
  k = 0;
  while (i < leftArr.length && k < rightArr.length) {
    if (leftArr[i] > rightArr[k]) {
      mergedArr.push(rightArr[k]);
      k++;
    } else {
      mergedArr.push(leftArr[i]);
      i++;
    }
  }
  while (i < leftArr.length) {
    mergedArr.push(leftArr[i]);
    i++;
  }
  while (k < rightArr.length) {
    mergedArr.push(rightArr[k]);
    k++;
  }

  return [mergeCnt, mergedArr];
}
