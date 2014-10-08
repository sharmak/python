# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 23:06:53 2014

@author: admin
"""
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right
class BST(object):
    def __init__(self, root):
        self.root = root
        
    def _insert(self, root, node):
        if root is None:
            return node
        elif node.val > root.val:
            root.right = self._insert(root.right, node)
            return root
        else:
            root.left = self._insert(root.left, node)
            return root
    def insert(self, tn):
        self._insert(self.root, tn)
    def _in_order(self, root):
        if root is None:
            return None
        self._in_order(root.left)
        print root.val
        self._in_order(root.right)
        
    def inOrder(self):
        self._in_order(self.root)
        
    def _pre_order(self, root):
        if root is None:
            return None
        print root.val
        self._pre_order(root.left)
        self._pre_order(root.right)
        
    def preOrder(self):
        self._pre_order(self.root)
    def _lca(self, root, n1, n2):
        print root.val, n1.val, n2.val
        if root is None:
            return None
        if (root.val >= n1.val) and (root.val <= n2.val):
            return root.val
        elif (root.val <= n1.val) and (root.val >= n2.val):
            return root.val
        elif (root.val > n1.val) and (root.val > n2.val):
            return self._lca(root.left, n1, n2)
        elif (root.val < n1.val) and (root.val < n2.val):
            return self._lca(root.right, n1, n2)
    def lca(self, v1, v2):
        n1 = TreeNode(v1)
        n2 = TreeNode(v2)
        return self._lca(self.root, n1, n2)
        
        
        
if __name__ == '__main__':
    n1 = TreeNode(2)
    n2 = TreeNode(1)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    t = BST(n1)
    t.insert(n4)
    t.insert(n3)
    t.insert(n2)
    #t.inOrder()
    #t.preOrder()
    print t.lca(1,2)
    