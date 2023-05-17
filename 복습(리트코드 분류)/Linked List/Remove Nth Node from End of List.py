class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        def getNodeLength(h):
            length = 0
            cur = h
            while cur:
                length += 1
                cur = cur.next
            return length

        length = getNodeLength(head)
        
        target = length - n
        
        if target == 0:
            head = head.next
            return head
     
        next_idx = 1
        cur_node = head

        while next_idx != target:
            cur_node = cur_node.next
            next_idx += 1

        if (cur_node.next is not None): cur_node.next = cur_node.next.next
        return head
            