class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function findLeftRightRoot(preorder, inorder) {
  if (!preorder.length) return null;

  const root = new Node(preorder[0]);
  const idx = inorder.indexOf(preorder[0]);

  root.left = findLeftRightRoot(preorder.slice(1, idx + 1), inorder.slice(0, idx));
  root.right = findLeftRightRoot(preorder.slice(idx + 1), inorder.slice(idx + 1));

  return root;
}

var buildTree = function (preorder, inorder) {
  const root = findLeftRightRoot(preorder, inorder);

  return root;
};
