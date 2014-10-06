# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 00:01:41 2014

@author: admin
"""
class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.node = value
        self.left = left
        self.right = right
class Tree(object):
    def __init__(self, root):
        self.root = root
    def _preOrder(self, cur):
        if cur is None:
            return None
        print cur.node
        self._preOrder(cur.left)
        self._preOrder(cur.right)
    def preOrder(self):
        self._preOrder(self.root)
    def _postOrder(self, cur):
        if cur is None:
            return None
        self._postOrder(cur.left)
        self._postOrder(cur.right)
        print cur.node
    def postOrder(self):
        self._postOrder(self.root)
    def _inOrder(self, cur):
        if cur is None:
            return None
        self._inOrder(cur.left)
        print cur.node
        self._inOrder(cur.right)
    def inOrder(self):
        self._inOrder(self.root)
    def _size(self, cur):
        #print cur
        if cur is None:
            return 0
        else:
            return self._size(cur.left) + self._size(cur.right) + 1
    def size(self):
        return self._size(self.root)
    def _height(self, cur):
        if cur is None:
            return 0
        else:
            return 1 + max(self._height(cur.left), self._height(cur.right))
    def height(self):
        return self._height(self.root)
        
        
def identical(cur1, cur2):
    #print cur1.node
    #print cur2.node
    if cur1 is not None \
        and cur2 is not None \
        and cur1.node == cur2.node:
        return True and identical(cur1.left, cur1.left)\
                    and identical(cur2.right, cur2.right)
    elif cur1 is None and cur2 is None:
        return True
    else:
        return False

def mirror(cur):
    if cur is None:
        return None
    l = mirror(cur.left)
    r = mirror(cur.right)
    cur1 = deepcopy(cur)
    cur1.left = r
    cur1.right = l
    return cur1
    
from copy import deepcopy
if __name__ == '__main__':
    n1 = TreeNode(3)
    n2 = TreeNode(2)
    n3 = TreeNode(1, left=n1, right=n2)
    t1 = Tree(n3)
    t2 = deepcopy(t1)
    #t.preOrder()
    #t.postOrder()
    #t.inOrder()
    #print t1.size()
    #print identical(t1.root, t2.root)
    #print t1.height()
    t3 = Tree(mirror(t2.root))
    t3.preOrder()
    t2.preOrder();