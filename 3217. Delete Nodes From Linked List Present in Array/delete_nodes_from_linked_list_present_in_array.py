# LeetCode Problem: 3217. Delete Nodes From Linked List Present in Array

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        values_to_remove = set(nums)
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next:
            if prev.next.val in values_to_remove:
                prev.next = prev.next.next
            else:
                prev = prev.next
        
        return dummy.next
