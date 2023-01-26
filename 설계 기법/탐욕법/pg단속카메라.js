function solution(routes) {
  var answer = 0;

  routes.sort((a, b) => {
    if (a[1] !== b[1]) return a[1] - b[1];
    return a[0] - b[0];
  });

  let cnt = 0;
  let last = -50000;
  for (let i = 0; i < routes.length; i++) {
    let [a, b] = routes[i];
    if (last >= a) continue;
    cnt++;
    last = b;
  }

  return cnt;
}
