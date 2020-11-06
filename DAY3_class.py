class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

s = ""

def serialize(node, s = ""):
    if not node:
        s += '* '
        return s
    s += (str(node.val) + " ")
    s = serialize(node.left, s)
    s = serialize(node.right, s)
    return s

print('After serialization : {}'.format(serialize(node)))

