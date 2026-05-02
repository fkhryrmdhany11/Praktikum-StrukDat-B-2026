DataAwal = ["google.com", "python.org"]

history_array = []

def tambah_pencarian_array(keyword):
    for data in DataAwal:
        if keyword in data:
            print(f"Keyword '{keyword}' ditemukan dalam data: {data}")
            break
    history_array.insert(0, keyword)

def tampilkan_history():
    if len(history_array) > 0:
        print('History Pencarian: ')
        for i in range(len(history_array)):
            print(f"{i+1}.{history_array[i]}")
    else:
        print("Belum ada pencarian yang dilakukan.")

for i in range(5):
    keyword = input('Masukkan Keyword: ')
    tambah_pencarian_array(keyword)
    tampilkan_history()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class HistoryLinkedList(Node):
    def __init__(self, data):
        super().__init__(data)

def tampilkan_history(head):
    currentNode = head
    i = 0
    while currentNode:
        print(f'{i+1}. {currentNode.data}')
        currentNode = currentNode.next
        i += 1

def tambah_pencarian_linked(head, newNode, position):
    if position == 1:
        newNode.next = head
        return newNode

    currentNode = head
    for _ in range(position - 2):
        if currentNode is None:
            break
        currentNode = currentNode.next

    newNode.next = currentNode.next
    currentNode.next = newNode
    return head

node1 = Node('google.com')
node2 = Node('python.org')
node3 = Node('stackoverflow.com')
node4 = Node('wikipedia.org')

node1.next = node2
node2.next = node3
node3.next = node4

print("\nBefore penambahan:")
tampilkan_history(node1)
newNode = Node(input("Masukkan keyword baru: "))
node1 = tambah_pencarian_linked(node1, newNode, 2)
print("\nAfter penambahan:")
tampilkan_history(node1)