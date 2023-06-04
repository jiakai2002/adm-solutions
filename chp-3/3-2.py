class Stack:
    def __init__(self, k):
        self.k = k
        self.storage = []

    def push(self, value):
        if self.isFull():
            raise Exception("Stack is Full")
        else:
            self.storage.append(value)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty")
        else:
            self.storage.pop()

    def peek(self):
        return self.storage[-1]

    def isEmpty(self):
        if len(self.storage) == 0:
            return True
        return False

    def isFull(self):
        if len(self.storage) == self.k:
            return True
        return False


def count_parentheses(pstr):
    # initialize pstack to store index of possible offenders
    pstack = Stack(20)
    count = 0
    for p in pstr:
        if p == '(':
            pstack.push(p)
        else:
            if not pstack.isEmpty():
                pstack.pop()
                count += 2
    return count

print(count_parentheses(')()(())()()))())))('))