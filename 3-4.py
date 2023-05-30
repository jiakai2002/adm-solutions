class Stack:
    def __init__(self, k):
        self.k = k
        self.storage = []
        self.min = None

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is Full")
        else:
            if not self.min or value > self.min:
                self.min = value            
            self.storage.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            self.storage.pop()

    def findmin(self):
        return self.min
    
    def isEmpty(self):
        if len(self.storage) == 0:
            return True
        return False

    def isFull(self):
        if len(self.storage) == self.k:
            return True
        return False
    
S = Stack(20)
S.push(1)
S.push(5)
S.push(2)
S.push(19)
print(S.findmin())

