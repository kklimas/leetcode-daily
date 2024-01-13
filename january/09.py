"""
Consider all the leaves of a binary tree, from left to right order,
the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def are_trees_leaf_similar(root1, root2):
    root_leafs1 = tree_leafs(root1)
    root_leafs2 = tree_leafs(root2)

    if len(root_leafs1) != len(root_leafs2):
        return False

    for index, leaf in enumerate(root_leafs1):
        if leaf != root_leafs2[index]:
            return False
    return True


def tree_leafs(root):
    if is_leaf(root):
        return [root.val]

    left_leaf = []
    right_leaf = []
    if root.left is not None:
        left_leaf = tree_leafs(root.left)
    if root.right is not None:
        right_leaf = tree_leafs(root.right)
    left_leaf.extend(right_leaf)
    return left_leaf


def is_leaf(node):
    return node.left is None and node.right is None


rot = TreeNode(1, TreeNode(2), TreeNode(5, TreeNode(2)))
print(tree_leafs(rot))
