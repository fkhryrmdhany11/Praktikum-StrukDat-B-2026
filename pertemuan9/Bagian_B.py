class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_tail(self, nama):
        new_node = Node(nama)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head
        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    def print_antrian(self):
        if self.head is None:
            return

        temp = self.head
        while True:
            print(temp.nama, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(kembali ke head)")

    def delete_head(self):
        if self.head is None:
            return

        # hanya 1 node
        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        # cari node terakhir
        last = self.head
        while last.next != self.head:
            last = last.next

        self.head = self.head.next
        last.next = self.head


# ====== TEST ======
cll = CircularLinkedList()

cll.insert_tail("Andi")
cll.insert_tail("Budi")
cll.insert_tail("Citra")
cll.insert_tail("Dina")

print("Antrian awal:")
cll.print_antrian()

# tambah Edo
cll.insert_tail("Edo")
print("\nSetelah tambah Edo:")
cll.print_antrian()

# hapus Andi
cll.delete_head()
print("\nSetelah Andi dilayani:")
cll.print_antrian()