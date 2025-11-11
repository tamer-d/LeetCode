# 86. Partition List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        low = ListNode()     # < x
        high = ListNode()    # >= x
        l = low
        h = high
        cur = head

        while cur:
            if cur.val < x:
                l.next = cur
                l = l.next
            else:
                h.next = cur
                h = h.next
            cur = cur.next

        h.next = None
        l.next = high.next
        return low.next
