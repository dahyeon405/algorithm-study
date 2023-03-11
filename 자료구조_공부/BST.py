# BST에서 값 삭제

class Node:
    def __init__(self, val):
        self.val = val

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def delete(self, val):
        def _delete(self, node, val): # 삭제 결과를 리턴해줌
            if node is None:
                return None
            if val < node.val:
                node.left = self._delete(self, node.left, val)
            if val > node.val:
                node.right = self._delete(self, node.right, val)
            else:
                if node.left is None: return node.right
                if node.right is None: return node.left
                min_val = self._get_min_val(node.right)
                node.val = min_val
                node.right = self._delete(self, node.right, min_val)
                return node
        self.root = _delete(self.root, val)

        return