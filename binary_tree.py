class Node:
    def __init__(self, key, value=None, left=None, right=None):
        if key is None:
            raise ValueError('Must supply key to node')
        if not isinstance(value, (int,None)):
            raise TypeError('value must be None or int')
        self.key = key
        self.value = value
        self.left = None
        self.right = None
def insert(root, key, value=None):
    return root

def search(root, key):
    return None
