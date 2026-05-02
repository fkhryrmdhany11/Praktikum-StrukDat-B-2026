class Node:
    def __init__(self, url):
        self.url = url
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.count == 0

    def push(self, url):
        baru = Node(url)
        
        if self.top == None:
            self.top = baru
        else:
            baru.next = self.top
            self.top = baru
        self.count += 1

    def pop(self):
        if self.is_empty():
            print('Kosong')
        else:
            url = self.top.url
            self.top = self.top.next
            self.count -= 1
            return url

    def peek(self):
        url = self.top.url
        return url

    def size(self):
        return self.count
    

a = StackLinkedList()
a.push('www.google.com')
a.push('www.instagram.com')
a.push('www.facebook.com')

print("LinkedList: ", end="")
print("Peek: ", a.peek())
print("Pop: ", a.pop())
print("LinkedList after Pop: ", end="")
print("isEmpty: ", a.is_empty())
print("Size: ", a.size())