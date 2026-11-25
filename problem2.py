from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(node):
    """Recursive count of total nodes in the tree."""
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    """Height in edges (empty tree -> -1, single node -> 0)."""
    if node is None:
        return -1
    left_height = height(node.left)
    right_height = height(node.right)
    return 1 + max(left_height, right_height)


def iterative_size(root):
    """Iterative count of total nodes using a level-order queue."""
    if root is None:
        return 0
    count = 0
    queue = deque([root])
    while queue:
        node = queue.popleft()
        count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return count


if __name__ == "__main__":
    # Build the tree from Problem 1
    root = Node(15)
    root.left = Node(10)
    root.right = Node(25)

    root.left.left = Node(4)
    root.left.right = Node(12)
    root.right.left = Node(20)
    root.right.right = Node(30)

    root.left.left.left = Node(2)
    root.left.left.right = Node(6)

    print(f"Recursive Size: {size(root)}")
    print(f"Iterative Size: {iterative_size(root)}")
    print(f"Height:         {height(root)}")