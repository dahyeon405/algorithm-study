function solution(queue1, queue2) {
  let q = queue1.concat(queue2);
  let sum = q.reduce((a, b) => a + b);

  if (sum % 2 !== 0) return -1;
  let halfsum = sum / 2;

  let halfsumSection = [];

  let startIdx = 0;
  let curSum = 0;

  let notFound = false; // k가 끝까지 갔는데 못 찾았을 경우
  for (let i = 0; i < q.length; i++) {
    if (q[i] > halfsum) return -1;
    if (notFound) break;
    for (let k = startIdx; k < q.length; k++) {
      curSum += q[k];

      if (curSum > halfsum) {
        startIdx = k;
        curSum = curSum - q[i] - q[k];
        break;
      }
      if (curSum === halfsum) {
        halfsumSection.push([i, k]);
        curSum -= q[i];
        startIdx = k + 1;
        break;
      }
      if (k === q.length - 1) {
        notFound = true;
      }
    }
  }

  if (halfsumSection.length === 0) return -1;
  const q2startIndex = queue1.length;
  const queue1Length = queue1.length;
  const queue2Length = queue2.length;

  function calculateCnt(section) {
    let [i, k] = section;
    if (k < queue1Length) {
      if (k === queue1Length - 1) return i;
      else {
        return queue2Length + i;
      }
    } else if (i < queue1Length && k < q.length - 1) {
      return i + k - queue1Length + 1;
    } else if (i >= queue1Length) {
      if (k === q.length - 1) return i - queue1Length;
      else {
        return k - queue1Length + 1 + i;
      }
    }
  }

  const countsArr = halfsumSection.map((el) => calculateCnt(el));
  const count = Math.min(...countsArr);

  return count;
}
