# LeetCode 654. Maximum Binary Tree
# https://leetcode.com/problems/maximum-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructMaximumBinaryTree(self, nums):
        # Cas de base
        if not nums:
            return None

        max_val = max(nums)
        max_index = nums.index(max_val)

        root = TreeNode(max_val)

        root.left = self.constructMaximumBinaryTree(nums[:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index+1:])

        return root