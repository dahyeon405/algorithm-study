function solution(n, s) {
  if (s < n) return [-1];
  let k = Math.floor(s / n);
  let remainder = s - k * n;

  let result = Array.from({ length: n }, () => k);

  let index = n - 1;
  while (remainder > 0) {
    result[index]++;
    remainder--;
    index--;
  }

  return result;
}
