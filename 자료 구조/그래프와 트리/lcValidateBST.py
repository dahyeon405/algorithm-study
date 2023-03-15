# 내 풀이.. 런타임은 중간인데 메모리가 매우 안 좋음

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValidTree(_root):

            if _root is None: return False

            left = isValidTree(_root.left)
            right = isValidTree(_root.right)

            if _root.left is None and _root.right is None:
                return [_root.val, _root.val]
            elif _root.left is None: 
                if right and right[0] > _root.val: return [_root.val, right[1]]
                else: return False
            elif _root.right is None:
                if left and left[1] < _root.val: return [left[0], _root.val]
                else: return False

            if left is False or right is False: return False
            l_min, l_max = left
            r_min, r_max = right
            if l_max >= _root.val or r_min <= _root.val: return False
            
            _min = min(l_min, r_min)
            _max = max(l_max, r_max)
            return [_min, _max]

        if isValidTree(root) is False: return False
        return True

# 다른 사람의 풀이
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValid(root, -2e31, 2e31-1)

    def isValid(self, root, min_val, max_val): 
        if not root: 
            return True
        
        if min and root.val <= min_val: 
            return False
        
        if max and root.val >= max_val:
            return False
        
        left_valid = self.isValid(root.left, min_val, root.val)
        right_valid = self.isValid(root.right, root.val, max_val)

        return left_valid and right_valid