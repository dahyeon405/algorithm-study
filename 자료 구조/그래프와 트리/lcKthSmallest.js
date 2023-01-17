var kthSmallest = function (root, k) {
  let result;

  function search(node, k) {
    if (!node) return 0;

    let size = 0;
    size += search(node.left, k);
    if (size === k - 1) result = node.val;
    size += search(node.right, k - size - 1);

    return size + 1;
  }

  search(root, k);
  return result;
};
