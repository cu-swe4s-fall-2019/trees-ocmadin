import unittest
import binary_tree as bt

class TestNode(unittest.TestCase):
    def test_input_params(self):
        self.assertRaises(ValueError,bt.Node,None)
        self.assertRaises(TypeError,bt.Node,'key',value=1.000)
        self.assertRaises(TypeError,bt.Node,'key','value')
        self.assertRaises(TypeError,bt.Node,'key',[1,1,1])
    def test_node_initialize(self):
        root = bt.Node('key',15)
        self.assertEqual(root.key,'key')
        self.assertEqual(root.value,15)
        self.assertEqual(root.left,None)
        self.assertEqual(root.right,None)