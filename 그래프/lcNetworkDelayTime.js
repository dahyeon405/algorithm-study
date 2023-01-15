// 벨만포드 알고리즘
var networkDelayTime = function (times, n, k) {
  const graph = {};
  times.forEach((el) => {
    let [u, v, w] = el;
    if (graph[u]) graph[u].push([v, w]);
    else graph[u] = [[v, w]];
  });

  let dist = Array.from({ length: n + 1 }, () => -1);
  dist[0] = 0;
  dist[k] = 0;

  for (let i = 0; i < n; i++) {
    let updated = false;
    for (let m = 1; m <= n; m++) {
      if (dist[m] !== -1) {
        const neighbors = graph[m];
        if (!neighbors) continue;
        for (let j = 0; j < neighbors.length; j++) {
          if (dist[neighbors[j][0]] === -1 || dist[neighbors[j][0]] > dist[m] + neighbors[j][1]) {
            dist[neighbors[j][0]] = dist[m] + neighbors[j][1];
            updated = true;
          }
        }
      }
    }
    if (!updated) break;
  }
  if (dist.indexOf(-1) !== -1) return -1;
  return Math.max(...dist);
};
