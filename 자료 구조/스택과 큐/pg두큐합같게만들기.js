function solution(queue1, queue2) {
  let q = queue1.concat(queue2);
  let sum = q.reduce((a, b) => a + b);

  if (sum % 2 !== 0) return -1;
  let halfsum = sum / 2;

  let halfsumSection = [];
  for (let i = 0; i < q.length; i++) {
    let curSum = 0;
    for (let k = i; k < q.length; k++) {
      curSum += q[k];
      if (curSum === halfsum) {
        halfsumSection.push([i, k]);
        break;
      }
    }
  }

  if (halfsumSection.length === 0) return -1;
  function calculateCnt(section) {
    let [i, k] = section;
    const q2startIndex = queue1.length;
    if (k < q2startIndex) {
      if (k === q2startIndex - 1) return i;
      else {
        return queue2.length + i;
      }
    } else if (i < q2startIndex && k < q.length - 1) {
      return i + k - q2startIndex + 1;
    } else if (i >= q2startIndex) {
      if (k === q.length - 1) return i - q2startIndex;
      else {
        return k - q2startIndex + 1 + queue1.length + i - q2startIndex;
      }
    }
  }

  const countsArr = halfsumSection.map((el) => calculateCnt(el));
  const count = Math.min(...countsArr);

  return count;
}
// 반 시간초과 ..
