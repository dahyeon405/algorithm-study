class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def _swap(node):
            if (node.next is None): return 
            cur = node.val
            nxt = node.next.val
            node.val, node.next.val = nxt, cur
            
        curNode = head
        while (curNode):
            _swap(curNode)
            if (curNode.next and curNode.next.next): curNode = curNode.next.next
            else: break

        return head
