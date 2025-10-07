# LeetCode Problem: 725. Split Linked List in Parts
# https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        base_size, extra = divmod(length, k)

        parts = []
        curr = head

        for i in range(k):
            part_head = curr
            size = base_size + (1 if i < extra else 0)
            for j in range(size - 1):
                if curr:
                    curr = curr.next

            if curr:
                next_part = curr.next
                curr.next = None
                curr = next_part

            parts.append(part_head)

        return parts
