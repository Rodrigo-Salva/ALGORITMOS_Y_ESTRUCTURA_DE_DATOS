from collections import defaultdict, deque

class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def build_tree_from_list(self, values):
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        self.root = nodes[0]
        for i in range(len(values)):
            if nodes[i]:
                left_index = 2 * i + 1
                right_index = 2 * i + 2
                if left_index < len(values):
                    nodes[i].left = nodes[left_index]
                if right_index < len(values):
                    nodes[i].right = nodes[right_index]

def vertical_order_traversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0)])  # (node, horizontal_distance)

    while queue:
        node, hd = queue.popleft()
        column_table[hd].append(node.val)
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    sorted_columns = sorted(column_table.items())  # Ordenar por distancia horizontal
    return [vals for _, vals in sorted_columns]

def test_vertical_order_traversal():
    print("Test 1")
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    print(vertical_order_traversal(tree1.root))  # [[4], [2], [1, 5], [3], [6]]

    print("Test 2")
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    print(vertical_order_traversal(tree2.root))  # [[3], [2], [1]]

    print("Test 3")
    tree3 = BinaryTree()
    print(vertical_order_traversal(tree3.root))  # []

    print("Test 4")
    tree4 = BinaryTree()
    tree4.build_tree_from_list([1])
    print(vertical_order_traversal(tree4.root))  # [[1]]

    print("Test 5")
    tree5 = BinaryTree()
    tree5.build_tree_from_list([1, 2, 3, 4, 5, 6, 7])
    print(vertical_order_traversal(tree5.root))  # [[4], [2], [1, 5, 6], [3], [7]]

test_vertical_order_traversal()
