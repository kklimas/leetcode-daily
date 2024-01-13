"""
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts
from the node with value start.

Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.

Return the number of minutes needed for the entire tree to be infected.
"""


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.parent = None
        self.left = left
        self.right = right
        self.infected = False


def rebuild_tree(node):
    if node.left is None and node.right is None:
        return

    if node.left is not None:
        node.left.parent = node
        rebuild_tree(node.left)

    if node.right is not None:
        node.right.parent = node
        rebuild_tree(node.right)


def find_node(root: Node, value: int):
    if root.val == value:
        return root
    node_left, node_right = None, None
    if root.left is not None:
        node_left = find_node(root.left, value)
    if root.right is not None:
        node_right = find_node(root.right, value)
    if node_left is not None:
        return node_left
    return node_right


def is_infected(node: Node):
    return node is None or node.infected


def longest_path(node: Node):
    node.infected = True

    if is_infected(node.parent) and is_infected(node.left) and is_infected(node.right):
        return 1

    p, l, r = 0, 0, 0

    parent = node.parent
    left_child = node.left
    right_child = node.right

    if not is_infected(parent):
        p = longest_path(parent)

    if not is_infected(left_child):
        l = longest_path(left_child)

    if not is_infected(right_child):
        r = longest_path(right_child)

    return max(p, l, r) + 1


def amount_of_time(root, start):
    rebuild_tree(root)
    start_node = find_node(root, start)
    return longest_path(start_node) - 1


root = Node(1, Node(5, None, Node(4, Node(9), Node(2))), Node(3, Node(10), Node(6)))
root2 = Node(1)
print(amount_of_time(root, 6))
