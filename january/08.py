"""
Given the root node of a binary search tree and two integers low and high, return the sum of values of all
 nodes with a value in the inclusive range [low, high].
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum(root, low, high):
    if root.left is None and root.right is None:
        return root.val if in_bound(root.val, low, high) else 0

    left_sum = 0
    right_sum = 0
    current_value = root.val if in_bound(root.val, low, high) else 0

    if root.left is not None:
        left_sum = range_sum(root.left, low, high)
    if root.right is not None:
        right_sum = range_sum(root.right, low, high)

    return left_sum + right_sum + current_value


def in_bound(value, low, high):
    return low <= value and value <= high
