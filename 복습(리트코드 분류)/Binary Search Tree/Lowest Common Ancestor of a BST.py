class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        result = root

        def hasPAndQ(node):
            nonlocal result
            has = [False, False]
            if node is None: return [False, False]
            
            if node.val == p.val: has[0] = True
            if node.val == q.val: has[1] = True

            has_left = hasPAndQ(node.left)
            has_right = hasPAndQ(node.right)
            if has_left is None or has_right is None: return

            has[0] = True if has[0] or has_left[0] or has_right[0] else False
            has[1] = True if has[1] or has_left[1] or has_right[1] else False


            if has[0] and has[1]: 
                result = node
                return
 
            return has

        hasPAndQ(root)

        return result