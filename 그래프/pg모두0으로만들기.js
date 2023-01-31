// 30% 정도 런타임 에러 (아마도 호출 스택 초과)
function solution(a, edges) {
  const tree = new Array(a.length).fill().map(() => []);
  edges.forEach((el) => {
    let [a, b] = el;
    tree[a].push(b);
    tree[b].push(a);
  });

  const total = a.reduce((x, y) => x + y, 0);
  if (total !== 0) return -1;

  let cnt = 0;
  const checked = Array.from({ length: a.length }, () => false);

  function dfs(k) {
    checked[k] = true;

    const neighbors = tree[k];
    for (let j = 0; j < neighbors.length; j++) {
      let el = neighbors[j];
      if (!checked[el]) {
        const val = dfs(el);
        cnt += Math.abs(val);
        a[k] += val;
      }
    }

    return a[k];
  }

  for (let i = 0; i < a.length; i++) {
    if (!checked[i]) {
      dfs(i);
    }
  }

  return cnt;
}
