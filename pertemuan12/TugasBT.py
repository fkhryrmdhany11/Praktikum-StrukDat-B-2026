class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert_manual(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')

def pre_order(node):
    if node is not None:
        print(node.data, end=' ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node is not None:
        in_order(node.left)
        print(node.data, end=' ')
        in_order(node.right)

def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end=' ')

def get_leaf_nodes(node, leaves=None):
    if leaves is None:
        leaves = []
    if node is not None:
        if node.left is None and node.right is None:
            leaves.append(node.data)
        else:
            get_leaf_nodes(node.left, leaves)
            get_leaf_nodes(node.right, leaves)
    return leaves

print()
print("=" * 38)
print("SISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("=" * 38)
print("[INFO] Membangun Struktur Gudang...")

tree = BinaryTree()

tree.insert_manual()
print("[INFO] Struktur berhasil dibuat.")
print()
print("HASIL AUDIT:")
print("1. Pre-Order  : ", end='')
pre_order(tree.root)
print()
print("2. In-Order   : ", end='')
in_order(tree.root)
print()
print("3. Post-Order : ", end='')
post_order(tree.root)
print()

leaf_nodes = get_leaf_nodes(tree.root)
leaf_str = ", ".join(leaf_nodes)
print(f"[DATA] Gudang Ujung (Leaf Nodes): {leaf_str}")
print("=" * 38)
print("Audit Selesai!")