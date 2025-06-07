class AVLNode:
    def __init__(self, key):
        self.key = key  # The value of the node
        self.left = None  # Left child
        self.right = None  # Right child
        self.height = 1  # Height of this node (leaf node starts with height 1)

class AVLTree:
    def insert(self, root, key):
        # Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor of this node
        balance = self.get_balance(root)

        # If the node becomes unbalanced, apply rotations:

        # Case 1 - Left Left
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Case 3 - Left Right
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        # Return the unchanged node pointer
        return root

    def get_height(self, node):
        # Return the height of a node or 0 if null
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        # Return the balance factor: left height - right height
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Return new root
        return y

    def inorder(self, root):
        # In-order traversal of the tree (sorted order)
        if root:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

def test_avl_insert():
    avl = AVLTree()

    root = None
    for val in [10, 20, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1 (RR):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [30, 20, 10]:
        root = avl.insert(root, val)
    print("🧪 Test 2 (LL):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [30, 10, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 3 (LR):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [10, 30, 20]:
        root = avl.insert(root, val)
    print("🧪 Test 4 (RL):", end=" ")
    avl.inorder(root)
    print()

    avl = AVLTree()
    root = None
    for val in [15, 10, 20, 25, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 5 (Balanced):", end=" ")
    avl.inorder(root)
    print()

test_avl_insert()
