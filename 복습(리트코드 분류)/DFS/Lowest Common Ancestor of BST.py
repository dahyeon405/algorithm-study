class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_val = p.val
        q_val = q.val

        q = []
        checked_val = 10**9 + 1
        
        # q에 추가
        def addToQueue(node):
            if node is None: return
            q.append(node)
            addToQueue(node.left)
            addToQueue(node.right)
        
        addToQueue(root)

        while q:
            cur = q.pop()

        
            # 종결 조건
            hasP = cur.val == p_val or (cur.left and cur.left.val == p_val) or (cur.right and cur.right.val == p_val)
            hasQ = cur.val == q_val or (cur.left and cur.left.val == q_val) or (cur.right and cur.right.val == q_val)
            if (hasP and hasQ): return cur

            if cur.left:
                if (cur.left.val == p_val or cur.left.val == q_val):
                    cur.val = cur.left.val
                elif cur.left.val == checked_val: 
                    cur.val = checked_val

            if cur.right:
                if cur.right.val == p_val or cur.right.val == q_val:
                    cur.val = cur.right.val