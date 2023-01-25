function solution(n, stations, w) {
  let sum = 0;
  let lastIndex = 1;
  const range = 2 * w + 1;

  for (let i = 0; i < stations.length; i++) {
    let startIndex = stations[i] - w - 1;
    if (startIndex >= lastIndex) {
      sum += Math.ceil((startIndex - lastIndex + 1) / range);
    }
    lastIndex = stations[i] + w + 1;
    if (lastIndex > n) return sum;
  }
  if (lastIndex > n) return sum;
  sum += Math.ceil((n - lastIndex + 1) / range);
  return sum;
}
