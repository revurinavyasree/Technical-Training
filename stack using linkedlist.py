class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def push(self):
        value = input("Enter value to push: ")
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print("Pushed", value)
        
    def pop(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            t = self.top.data
            self.top = self.top.next
            print("Popped", t)
    def peek(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            print("Top of stack:", self.top.data)
    
    def display(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            temp = self.top
            print("Stack elements:")
            while temp is not None:
                print(temp.data)
                temp = temp.next
    def is_empty(self):
        if self.top is None:
            print("Stack is empty!")
        else:
            print("Stack is not empty.")

# Drive Code
s = Stack()
# Menu-driven interface
while True:
    print("\n--- Stack Menu ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display Stack")
    print("5. Check if Empty")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        s.push()
    elif choice == '2':
        s.pop()
    elif choice == '3':
        s.peek()
    elif choice == '4':
        s.display()
    elif choice == '5':
        s.is_empty()
    elif choice == '6':
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Please select from 1 to 6.")
