function createGraph(node, parent) {
  if (!node) return;
  const neighbor = [];

  if (node.left) {
    neighbor.push(node.left.val);
    createGraph(node.left, node.val);
  }
  if (node.right) {
    neighbor.push(node.right.val);
    createGraph(node.right, node.val);
  }
  if (parent !== null) neighbor.push(parent);
  adjacencyList[node.val] = neighbor;
}

var distanceK = function (root, target, k) {
  toVisit.push(target);
  dist[targetIndex] = 0;
  let result = [];
  while (toVisit.length) {
    let next = toVisit.shift();
    let nextDist = dist[next];
    if (nextDist === k) {
      result.push(next);
      continue;
    }
    let nextAdjs = [Math.floor((next - 1) / 2), next * 2 + 1, next * 2 + 2];
    nextAdjs.forEach((el) => {
      if (el !== null && dist[el] === -1) {
        toVisit.push(el);
        dist[el] = nextDist + 1;
      }
    });
  }
  return result;
};
