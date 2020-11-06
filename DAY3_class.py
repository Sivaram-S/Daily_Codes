class Node:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

node = Node('root', Node('left', Node('left.left')), Node('right'))

def serialize(node, s = ""):
    if not node:
        s += '* '
        return s
    s += (str(node.val) + " ")
    s = serialize(node.left, s)
    s = serialize(node.right, s)
    return s


i = 0

def deserialize(s):
    global i
    if s[i] == '*':
        i += 2
        return None
    else:
        space = s[i:].find(" ")
        sp = space + i
        node = Node(s[i:sp])
        i = sp+1
        node.left = deserialize(s)
        node.right = deserialize(s)
        return node

print('After serialization : {}'.format(serialize(node)))
assert deserialize(serialize(node)).left.left.val == 'left.left'
i = 0
x = deserialize(serialize(node))
print(x.left.left.val)


