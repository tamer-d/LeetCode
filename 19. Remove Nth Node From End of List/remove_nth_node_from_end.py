
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        index_to_remove = length - n
        
        if index_to_remove == 0:
            return head.next
        
        curr = head
        for _ in range(index_to_remove - 1):
            curr = curr.next
        
        curr.next = curr.next.next
        
        return head
