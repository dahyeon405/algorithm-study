function solution(begin, target, words) {
  const selected = Array.from({ length: words.length }, () => false);

  function canConvert(from, to) {
    let diffCnt = 0;
    for (let i = 0; i < from.length; i++) {
      if (from[i] !== to[i]) diffCnt++;
    }
    if (diffCnt === 1) return true;
    return false;
  }

  if (!words.includes(target)) return 0;
  let min = words.length;
  function dfs(word, cnt) {
    // 일치할 경우 종료
    if (word === target) {
      if (min > cnt) min = cnt;
      return;
    }

    for (let i = 0; i < words.length; i++) {
      if (!selected[i] && canConvert(word, words[i])) {
        selected[i] = true;
        dfs(words[i], cnt + 1);
        selected[i] = false;
      }
    }
    return;
  }

  dfs(begin, 0);

  return min;
}
