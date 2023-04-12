# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:

        def getMin(node):
            min_val = node.val
            min_node = node
            if node.left:
                left_min = getMin(node.left)            
                if left_min.val < min_val: 
                    min_val = left_min.val
                    min_node = left_min
            if node.right:
                right_min = getMin(node.right)
                if right_min.val < min_val: 
                    min_val = right_min.val
                    min_node = right_min
            return min_node

        def getMax(node):
            max_val = node.val 
            max_node = node
            if node.left:
                left_max = getMax(node.left)
                if left_max.val > max_val: 
                    max_node = left_max
                    max_val = left_max.val
            if node.right:
                right_max = getMax(node.right)
                if right_max.val > max_val: 
                    max_val = right_max.val
                    max_node = right_max
            return max_node

        def isSwapped(node):
            max_left, min_right = node, node
            if node.left: max_left = getMax(node.left)
            if node.right: min_right = getMin(node.right)

            if max_left.val > node.val and min_right.val < node.val:
                max_left.val, min_right.val = min_right.val, max_left.val
                return True
            elif max_left.val > node.val:
                max_left.val, node.val = node.val, max_left.val
                return True
            elif min_right.val < node.val:
                min_right.val, node.val = node.val, min_right.val
                return True

            return False


        def _recoverTree(node):
            if node is None: return False
            if (isSwapped(node)): return True
            
            if (_recoverTree(node.left)): return True
            if (_recoverTree(node.right)): return True

            return False

        _recoverTree(root)

# 타인의 답안
class Solution(object): 
    def recoverTree(self, root): # O(lg(n)) space
        pre = first = second = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                break
            node = stack.pop()
            if not first and pre and pre.val > node.val:
                first = pre
            if first and pre and pre.val > node.val:
                second = node
            pre = node
            root = node.right
        first.val, second.val = second.val, first.val
      
    def recoverTree1(self, root): # O(n+lg(n)) space  
        res = []
        self.dfs(root, res)
        first, second = None, None
        for i in range(len(res)-1):
            if res[i].val > res[i+1].val and not first:
                first = res[i]
            if res[i].val > res[i+1].val and first:
                second = res[i+1]
        first.val, second.val = second.val, first.val
        
    def dfs(self, root, res):
        if root:
            self.dfs(root.left, res)
            res.append(root)
            self.dfs(root.right, res)