class Node:
    def __init__(self, payload, parent=None):
        self.payload = payload
        self.parent = parent
        self.action = None

    def equal(self, node):
        return self.payload.equal(node.payload)

    def clone(self):
        return Node(self.payload.clone(), self)

    def h(self):
        return self.payload.h()

    def move(self, action):
        self.action = action
        self.payload.move(action)

    def isSolve(self):
        return self.payload.isSolve()

    def possibleAction(self, translated=False):
        return self.payload.possibleAction(translated)

    def g(self):
        i = 0
        node = self
        while node.parent is not None:
            i += 1
            node = node.parent
        return i
