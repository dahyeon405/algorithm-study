var inorderTraversal = function (root) {
  const result = [];

  function traverse(node) {
    if (!node) return;
    const left = traverse(node.left);
    result.push(node.val);
    const right = traverse(node.right);
  }

  traverse(root);
  return result;
};

// iterative way

var inorderTraversal2 = function (root) {
  const result = [];
  const queue = [];

  function pushToQueue(node) {
    let nextNode = node;
    while (nextNode) {
      queue.push(nextNode);
      nextNode = nextNode.left;
    }
  }

  pushToQueue(root);
  while (queue.length) {
    let node = queue.pop();
    result.push(node.val);
    pushToQueue(node.right);
  }

  return result;
};
