class Stack[T=str]:
    def __init__(self): self.items: list[T] = []
    def push(self, item: T): self.items.append(item)
    def size(self): return len(self.items)
    def peek(self): return self.items[-1] if self.items else None
    def pop(self): return self.items.pop() if self.items else None
    def clear(self): self.items.clear()
    def iter(self): return iter(self.items)
