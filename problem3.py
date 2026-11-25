class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Insert key into the BST, ignoring duplicates."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key) -> bool:
        """Return True if key exists in the BST, False otherwise."""
        return self._search(self.root, key)

    def _search(self, node, key) -> bool:
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        """Remove key from the BST if present."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            # Case 1 & 2: zero or one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: two children (replace with inorder successor)
            successor = self._min_value_node(node.right)
            node.data = successor.data
            node.right = self._delete(node.right, successor.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def inorder(self) -> list:
        """Return a sorted list of all keys in the BST."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)


if __name__ == "__main__":
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())    # line A
    print(bst.search(35))   # line B
    print(bst.search(99))   # line C
    bst.delete(20)          # leaf
    bst.delete(40)          # two children
    print(bst.inorder())    # line D