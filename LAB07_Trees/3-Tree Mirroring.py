# Definition of a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to mirror the binary tree
def mirror_tree(root):
    if root is None:
        return None
    # Swap the left and right subtrees
    root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root

# Helper function for in-order traversal (used to visually verify the tree structure)
def inorder_traversal(root):
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right) if root else []

# Test cases for the mirror_tree function
def test_mirror_tree():
    # Test Case 1: Normal binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    mirror_tree(root)
    print("Test 1 (Normal Tree):", inorder_traversal(root))  # Expected [3, 1, 5, 2, 4]

    # Test Case 2: Empty tree
    empty_tree = None
    mirror_tree(empty_tree)
    print("Test 2 (Empty Tree):", inorder_traversal(empty_tree))  # Expected []

    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    mirror_tree(single_node)
    print("Test 3 (Single Node):", inorder_traversal(single_node))  # Expected [1]

    # Test Case 4: Tree with only left children
    left_only = TreeNode(1)
    left_only.left = TreeNode(2)
    left_only.left.left = TreeNode(3)
    mirror_tree(left_only)
    print("Test 4 (Only Left Children):", inorder_traversal(left_only))  # Expected [3, 2, 1]

    # Test Case 5: Perfect binary tree
    perfect = TreeNode(1)
    perfect.left = TreeNode(2)
    perfect.right = TreeNode(3)
    perfect.left.left = TreeNode(4)
    perfect.left.right = TreeNode(5)
    perfect.right.left = TreeNode(6)
    perfect.right.right = TreeNode(7)
    mirror_tree(perfect)
    print("Test 5 (Perfect Tree):", inorder_traversal(perfect))  # Expected [7, 3, 6, 1, 5, 2, 4]

test_mirror_tree()
