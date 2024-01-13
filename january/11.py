"""
Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b
where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
"""
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def max_ancestor_diff(node):
    if node.left is None and node.right is None:
        return 0, node.val, node.val

    l_diff, l_min, l_max = 0, inf, -1
    r_diff, r_min, r_max = 0, inf, -1

    if node.right is not None:
        r_diff, r_min, r_max = max_ancestor_diff(node.right)

    if node.left is not None:
        l_diff, l_min, l_max = max_ancestor_diff(node.left)

    best_diff = max(l_diff, r_diff, abs(node.val - min(l_min, r_min)), abs(node.val - max(l_max, r_max)))
    best_min = min(l_min, r_min, node.val)
    best_max = max(l_max, r_max, node.val)

    return best_diff, best_min, best_max




root = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))),
                TreeNode(10, None, TreeNode(14, TreeNode(13))))

root2 = TreeNode(2, TreeNode(0, TreeNode(4, TreeNode(3, TreeNode(1)))))
# print(max_ancestor_diff(root))
print(max_ancestor_diff(root2))
