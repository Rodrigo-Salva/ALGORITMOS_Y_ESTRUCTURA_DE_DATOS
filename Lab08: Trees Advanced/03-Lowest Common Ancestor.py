class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        """Builds a binary tree from a list of values."""
        if not values:
            return

        nodes = [TreeNode(val) if val is not None else None for val in values]
        self.root = nodes[0]

        for i in range(len(values)):
            if nodes[i] is not None:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(nodes):
                    nodes[i].left = nodes[left_index]
                if right_index < len(nodes):
                    nodes[i].right = nodes[right_index]

def lowest_common_ancestor(root, p, q):
    """Finds the lowest common ancestor of nodes with values p and q."""
    if root is None:
        return None
    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left and right:
        return root
    return left if left else right

def test_lowest_common_ancestor():
    """Test the lowest_common_ancestor function."""
    
    # Test Case 1: Nodes in different subtrees
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    lca1 = lowest_common_ancestor(tree1.root, 4, 6)
    print("LCA of 4 and 6:", lca1.value if lca1 else "Not found")  # Expected: 1
    
    # Test Case 2: One node is ancestor of the other
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, 3, 4])
    lca2 = lowest_common_ancestor(tree2.root, 2, 4)
    print("LCA of 2 and 4:", lca2.value if lca2 else "Not found")  # Expected: 2
    
    # Test Case 3: Nodes are siblings
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, 2, 3])
    lca3 = lowest_common_ancestor(tree3.root, 2, 3)
    print("LCA of 2 and 3:", lca3.value if lca3 else "Not found")  # Expected: 1
    
    # Test Case 4: One node is the root
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1, 2, 3])
    lca4 = lowest_common_ancestor(tree4.root, 1, 3)
    print("LCA of 1 and 3:", lca4.value if lca4 else "Not found")  # Expected: 1
    
    # Test Case 5: Node not in the tree
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3])
    lca5 = lowest_common_ancestor(tree5.root, 9, 3)
    print("LCA of 9 and 3:", lca5.value if lca5 else "Not found")  # Expected: Not found

# Run test cases
test_lowest_common_ancestor()
