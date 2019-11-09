import unittest
import binary_tree as bt

class TestNode(unittest.TestCase):
    def test_input_params(self):
        self.assertRaises(ValueError,bt.Node,None)
        self.assertRaises(TypeError,bt.Node,'key',value=1.000)
        self.assertRaises(TypeError,bt.Node,'key','value')
        self.assertRaises(TypeError,bt.Node,'key',[1,1,1])
    def test_node_initialize(self):
        root = bt.Node(15,'val')
        self.assertEqual(root.key,15)
        self.assertEqual(root.value,'val')
        self.assertEqual(root.left,None)
        self.assertEqual(root.right,None)

class TestInsert(unittest.TestCase):
    def test_input_params(self):
        self.assertRaises(ValueError,bt.insert,None,None,12)
        self.assertRaises(ValueError,bt.insert,None,12,None)
        self.assertRaises(TypeError,bt.insert,None,1.1,1.02)
        self.assertRaises(TypeError,bt.insert,None,[1,1,1],1.1)
    def test_no_root(self):
        root = None
        root = bt.insert(root,15,'val')
        self.assertEqual(root.key,15)
        self.assertEqual(root.value,'val')
        self.assertEqual(root.left,None)
        self.assertEqual(root.right,None)
    def test_root_exists_left_node(self):
        root = None
        root = bt.insert(root,15,'val')
        root = bt.insert(root,12,'val2')
        self.assertEqual(root.left.value,'val2')
        self.assertEqual(root.right,None)
    def test_root_exists_right_node(self):
        root = None
        root = bt.insert(root,15,'val')
        root = bt.insert(root,16,'val2')
        self.assertEqual(root.right.value,'val2')
        self.assertEqual(root.left,None)
    def test_recursion_left(self):
        root = None
        root = bt.insert(root,15,'val')
        root = bt.insert(root,14,'val2')
        root = bt.insert(root,13,'val3')
        self.assertEqual(root.value, 'val')
        self.assertEqual(root.left.value,'val2')
        self.assertEqual(root.left.left.value,'val3')
        self.assertEqual(root.right,None)
    def test_recursion_right(self):
        root = None
        root = bt.insert(root,15,'val')
        root = bt.insert(root,16,'val2')
        root = bt.insert(root,17,'val3')
        self.assertEqual(root.value, 'val')
        self.assertEqual(root.right.value,'val2')
        self.assertEqual(root.right.right.value,'val3')
        self.assertEqual(root.left,None)
