from typing import List

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        capacity.sort(reverse=True)

        used_boxes = 0
        current_capacity = 0

        for cap in capacity:
            current_capacity += cap
            used_boxes += 1
            if current_capacity >= total_apples:
                return used_boxes

        return used_boxes
