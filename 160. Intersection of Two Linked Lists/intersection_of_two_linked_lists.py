class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None

        a, b = headA, headB

        # Avance les deux pointeurs jusqu'à ce qu'ils se croisent
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA

        return a  # Soit le nœud d’intersection, soit None
