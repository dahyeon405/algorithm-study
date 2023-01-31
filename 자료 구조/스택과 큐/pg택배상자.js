function solution(order) {
  const subcontainer = [];
  let nextEl = 1;
  let cnt = 0;
  let i = 0;

  while (i < order.length && nextEl <= order.length) {
    if (order[i] === nextEl) {
      cnt++;
      if (nextEl < order.length) nextEl++;
      i++;
    } else if (subcontainer[subcontainer.length - 1] === order[i]) {
      subcontainer.pop();
      cnt++;
      i++;
    } else if (order[i] > nextEl) {
      subcontainer.push(nextEl);
      if (nextEl < order.length) nextEl++;
    } else {
      break;
    }
  }

  return cnt;
}
