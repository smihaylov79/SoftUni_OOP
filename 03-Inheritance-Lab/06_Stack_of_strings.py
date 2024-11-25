class Stack:
    def __init__(self, *args):
        self.data = [str(el) for el in args]

    def push(self, element):
        return self.data.append(str(element))

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        return "["+", ".join(reversed(self.data))+"]"


stack = Stack(1,2,3,4,5)
stack.push("apple")
stack.push("carrot")
print(stack)

