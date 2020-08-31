from utils.tree import Node

def astar(node):
    return runAstar([(0, Node(node))], 0, [node])

def isIn(node, list):
    for elem in list:
        if node.equal(elem):
            return True

    return False

def runAstar(nodes, depth=0, memory=[]):
    while nodes:
        node = nodes.pop()[1]
        if node.isSolve():
            print("Solution found")
            actions = []
            while node.parent is not None:
                actions.append(node.action)
                node = node.parent

            actions.reverse()
            return actions

        childs = []
        for action in node.possibleAction(True):
            child = node.clone()
            child.move(action)
            if not isIn(child.payload, memory):
                g = child.g()
                h = child.h()
                f = g + h
                nodes.append((f, child))

        memory.append(node.payload)
        nodes.sort(key=lambda n:n[0], reverse=True) # [4, 3, 2, 1]
        depth += 1
