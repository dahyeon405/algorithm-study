class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def countMatchedPaths(_root):
            def _countMatchedPaths(node, total):
                if node is None: return 0
                _paths = 0
                _total = node.val + total
                if _total == targetSum: _paths += 1
                _paths += (_countMatchedPaths(node.left, _total)+_countMatchedPaths(node.right, _total))

                return _paths
            paths = _countMatchedPaths(_root, 0)
            return paths

        def countAllPaths(_root):
            if _root is None: return 0
            
            total = countMatchedPaths(_root)
            total += countAllPaths(_root.left)
            total += countAllPaths(_root.right)

            return total
        
        return countAllPaths(root)