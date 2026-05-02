class StackListList:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, url):
        self.items.append(url)

    def pop(self):
        if self.is_empty():
            return "StackList is empty"
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return "StackList is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)
    
a = StackListList()
a.push('www.google.com')
a.push('www.instagram.com')
a.push('www.facebook.com')

print("Stack: ", a.items)
print("Pop: ", a.pop())
print("Stack after Pop: ", a.items)
print("Peek: ", a.peek())
print("isEmpty: ", a.is_empty())
print("Size: ", a.size())