class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(root, min_val, max_val):
            if not root: return True
            if min_val is not None and root.val <= min_val:
                return False
            if max_val is not None and root.val >= max_val:
                return False
            
            left_valid = isValid(root.left, min_val, root.val)
            right_valid = isValid(root.right, root.val, max_val)

            return left_valid and right_valid

        return isValid(root, -2e31, 2e31-1)