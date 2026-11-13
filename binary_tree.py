r"""
Assessment 3.3 - Binary Tree (RODRIGUEZ)

Tree structure (from the diagram):

                R
           /        \
          O          D
        /   \       /   \
       R     I     G     U
     /   \
    E     Z

Traversals:
  BFS (level order) -> R O D R I G U E Z
  DFS (preorder)    -> R O R E Z I D G U
"""

from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_rodriguez_tree():
    """Build the binary tree shown in the diagram."""
    e = Node("E")
    z = Node("Z")
    r2 = Node("R", e, z)      # left child of O
    i = Node("I")             # right child of O
    o = Node("O", r2, i)

    g = Node("G")             # left child of D
    u = Node("U")             # right child of D
    d = Node("D", g, u)

    return Node("R", o, d)    # root


def bfs(root):
    """Breadth-First Search (level order): visit level by level, left to right."""
    order = []
    if root is None:
        return order

    queue = deque([root])
    while queue:
        node = queue.popleft()
        order.append(node.value)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
    return order


def dfs(root):
    """Depth-First Search (preorder): root, then left subtree, then right subtree."""
    order = []

    def visit(node):
        if node is None:
            return
        order.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return order


def main():
    root = build_rodriguez_tree()

    print("Binary Tree - RODRIGUEZ")
    print("BFS (Breadth-First Search):", " - ".join(bfs(root)))
    print("DFS (Depth-First Search):  ", " - ".join(dfs(root)))


if __name__ == "__main__":
    main()
