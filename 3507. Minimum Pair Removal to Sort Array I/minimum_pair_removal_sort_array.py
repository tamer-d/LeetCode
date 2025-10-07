# LeetCode Problem: 3507. Minimum Pair Removal to Sort Array I
# Link: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-i/

import heapq

class Node:
    def __init__(self, val, idx):
        self.val = val
        self.idx = idx  
        self.prev = None
        self.next = None
        self.active = True  

def minimumOperations(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0

    nodes = [Node(nums[i], i) for i in range(n)]
    for i in range(1, n):
        nodes[i - 1].next = nodes[i]
        nodes[i].prev = nodes[i - 1]

    heap = []
    for i in range(n - 1):
        heapq.heappush(heap, (nodes[i].val + nodes[i + 1].val, nodes[i].idx, nodes[i]))

    operations = 0

    def remove_node(node: Node):
        node.active = False
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    while heap:
        s, _, left = heapq.heappop(heap)
        right = left.next
        if not right or not left.active or not right.active or left.next != right:
            continue

        new_val = s
        left.val = new_val
        remove_node(right)
        operations += 1

        if left.prev:
            heapq.heappush(heap, (left.prev.val + left.val, left.prev.idx, left.prev))
        if left.next:
            heapq.heappush(heap, (left.val + left.next.val, left.idx, left))


    return operations
