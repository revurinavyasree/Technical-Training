class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item,"pushed into stack")
    def pop(self):
        if self.is_empty():
            print("stack is empty.cannot be pop")
        else:
            removed=self.stack.pop()
            print(removed,"poped from stack")
    def peek(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("Top element is:",self.stack[-1])
    def is_empty(self):
        return len(self.stack)==0
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack elements:",self.stack)
    def count_stack(self):
        if self.is_empty():
            print("stackis empty")
        else:
            m=max(self.stack)
            print("count the stack:",self.stack.count(m))
s=Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(30)
s.push(23)
s.push(30)
s.display()
s.peek()
s.pop()
s.display()
s.count_stack()

