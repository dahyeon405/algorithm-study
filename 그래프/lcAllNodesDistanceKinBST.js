var distanceK = function (root, target, k) {
  const adjacencyList = {};
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
  createGraph(root, null);

  const toVisit = [];
  const visited = new Set();

  toVisit.push([target.val, 0]);
  visited.add(target.val);
  const result = [];
  while (toVisit.length) {
    let [next, dist] = toVisit.shift();
    if (dist === k) {
      result.push(next);
      continue;
    }
    let nextAdjs = adjacencyList[next];
    if (!nextAdjs) continue;
    nextAdjs.forEach((el) => {
      if (el !== null && !visited.has(el)) {
        toVisit.push([el, dist + 1]);
        visited.add(el);
      }
    });
  }
  return result;
};
