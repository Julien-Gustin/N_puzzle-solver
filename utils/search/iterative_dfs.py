def isIn(node, list):
    for elem in list:
        if node.equal(elem):
            return True

    return False

def iterative_deepening_search(node):
    depth = 0
    result = False
    actions = []
    while result is False:
        print(depth)
        result, actions = depth_limited_search(node, depth)
        depth += 1

    return actions


def depth_limited_search(node, limit):
    return recursive_dls(node, limit, [])

def recursive_dls(node, limit, memory=[]):

    if node.isSolve():
        return True, []

    elif limit == 0:
        return False, []

    for action in node.possibleAction(True):
        child = node.clone()
        child.move(action)

        if isIn(child, memory) is False:
            memory.append(child)
            result, actions = recursive_dls(child, limit -1, memory)
            if result:
                actions.append(action)
                return result, actions

    return False, []
