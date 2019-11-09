class Node:
    def __init__(self, key, value=None, left=None, right=None):
        if key is None:
            raise ValueError('Must supply key to node')
        if key is None:
            raise TypeError('Must supply key')
        elif not isinstance(key, int):
            raise TypeError('Key must be None or int')
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        
        
def insert(root, key, value=None):
    if value is None:
        raise ValueError('Must supply value to insert')
    if key is None:
        raise ValueError('Must supply value')
    elif not isinstance(key, int):
        raise TypeError('Key must be None or int')   
    if root is None:
        root = Node(key,value=value)
    else:
        if key > root.key:
            if root.right == None:
                root.right = Node(key,value=value)
            else:
                insert(root.right,key,value=value)
        else:
            if root.left == None:
                root.left = Node(key,value=value)
            else:
                insert(root.left,key,value=value)
    return root

def search(root, key):
    if key is None:
        raise ValueError('Must supply key to search')
    if not isinstance(key,int):
        raise TypeError('Key must be int')
    if root.key == key:
        return root.value
    elif key < root.key:
        if root.left is None:
            return None
        else:
            return search(root.left,key)
    elif key > root.key:
        if root.right is None:
            return None
        else:    
            return search(root.right,key)

