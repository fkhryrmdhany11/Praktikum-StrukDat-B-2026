class Node:
    def __init__(self, id, judul):
        self.id = id
        self.judul = judul
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, id, judul, node=None):
        if node is None:
            if self.root is None:
                self.root = Node(id, judul)
            else:
                self.insert(id, judul, self.root)
        else:
            if id < node.id:
                if node.left is None:
                    node.left = Node(id, judul)
                else:
                    self.insert(id, judul, node.left)
            else:
                if node.right is None:
                    node.right = Node(id, judul)
                else:
                    self.insert(id, judul, node.right)
    
    def search(self, id, node=None, _is_initial=True):
        if _is_initial and node is None:
            node = self.root
        
        if node is None:
            return None
        
        if id == node.id:
            return node
        elif id < node.id:
            return self.search(id, node.left, False)
        else:
            return self.search(id, node.right, False)
    
    def traversal_inorder(self, node=None, result=None):
        if result is None:
            result = []
            if node is None:
                node = self.root
            initial_call = True
        else:
            initial_call = False
        
        if node is not None:
            self.traversal_inorder(node.left, result)
            result.append((node.id, node.judul))
            self.traversal_inorder(node.right, result)
        
        if initial_call:
            return result
    
    def get_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left is not None:
            current = current.left
        return current
    
    def get_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right is not None:
            current = current.right
        return current
    
    def height(self, node=None, _is_initial=True):
        if _is_initial and node is None:
            node = self.root
        if node is None:
            return -1
        return 1 + max(self.height(node.left, False), self.height(node.right, False))
    
    def search_and_print(self, id):
        hasil = self.search(id)
        if hasil:
            print(f"[SEARCH] Mencari ID {id}... Ditemukan! Judul: {hasil.judul}")
        else:
            print(f"[SEARCH] Mencari ID {id}... Data tidak ditemukan.")

print("")
print("=" * 70)
print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("=" * 70)

katalog = BST()

buku_data = [(50, "Dasar Pemrograman"),
            (30, "Struktur Data"),
            (70, "Kecerdasan Buatan"),
            (20, "Matematika Diskrit"),
            (40, "Basis Data"),
            (60, "Jaringan Komputer"),
            (80, "Sistem Operasi")]


for id, judul in buku_data:
    katalog.insert(id, judul)
    print(f"[INSERT] Berhasil memasukkan: ID {id} - {judul}")


print("\n[INFO] Koleksi Buku (In-Order Traversal):")
koleksi = katalog.traversal_inorder()
for i, (id, judul) in enumerate(koleksi, 1):
    print(f"{i}. {id} - {judul}")


print("\n[PENCARIAN]")

katalog.search_and_print(60)
katalog.search_and_print(100)


print("\n[STATISTIK]")
min_buku = katalog.get_min()
max_buku = katalog.get_max()
print(f"[STATISTIK] ID Terkecil: {min_buku.id}")
print(f"[STATISTIK] ID Terbesar: {max_buku.id}")


print("\n[INFO] Tinggi (Height) Tree:", katalog.height())

print("\n" + "=" * 70)
print("Simulasi Selesai!")