class BSTNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val
        self.parent = None

    def insert(self, val):
        if not self.val:
            self.val = val

        elif val == self.val:
            return

        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTNode(val)

        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTNode(val)

    def search(self, val):
        if self.val == val:
            return True

        elif val > self.val:
            if self.right:
                return self.right.search(val)
            else:
                return False

        elif val < self.val:
            if self.left:
                return self.left.search(val)
            else:
                return False


def build_tree(elements):
    root = BSTNode(elements[0])
    for i in elements:
        root.insert(i)
    return root


def find_sum_pair_1(s1, s2, x):
    bst_s2 = build_tree(s2)
    for i in s1:
        if bst_s2.search(x - i):
            return True


def find_sum_pair_2(s1, s2, x):
    for i in s1:
        for j in s2:
            if x == i + j:
                return True
