var canFinish = function (numCourses, prerequisites) {
  const orderMap = new Map();
  const visited = Array.from({ length: numCourses }, () => 0);
  prerequisites.forEach((el) => {
    let [a, b] = el;
    if (orderMap.has(b)) orderMap.get(b).push(a);
    else orderMap.set(b, [a]);
  });
  // visited 0 은 미방문
  // visited 1 는 dfs 탐색 중 방문
  // visited 2 는 dfs 탐색 완료
  function isCyclic(i, visited) {
    if (visited[i] === 1) return true;
    visited[i] = 1;
    const nextCourses = orderMap.get(i) || [];
    for (let k = 0; k < nextCourses.length; k++) {
      if (visited[nextCourses[k]] === 2) continue;
      if (isCyclic(nextCourses[k], visited)) return true;
    }
    visited[i] = 2;
    return false;
  }
  for (let i = 0; i < numCourses; i++) {
    if (visited[i] !== 0) continue;
    if (isCyclic(i, visited)) return false;
  }
  return true;
};
