class Stack:
    def __init__(self):
         self.stack = []

    def check_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
        print(f"{data} is added to the stack")

    def pop(self):
        if(self.check_empty()):
            return "Stack is Empty"

        return self.stack.pop()

    def display(self):
        print("Stack is ",end="")
        for i in self.stack:
            print(i,end=" ")


stack = Stack()
print("Pushing operation in stack")
stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")
stack.display()
print("\nPopping operation in stack")
stack.pop()
stack.display()
