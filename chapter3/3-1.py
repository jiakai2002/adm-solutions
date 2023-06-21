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


def check_parentheses(pstr):
    # initialize pstack to store index of possible offenders
    pstack = Stack(20)
    for i in range(0, len(pstr)):
        if pstr[i] == "(":
            pstack.push(i)
        else:
            if not pstack.isEmpty():
                pstack.pop()
            else:
                return False, i
                break
    if pstack.isEmpty():
        return True
    else:
        # return index of first offender
        return False, pstack.storage[0]


print(check_parentheses("((((())"))
